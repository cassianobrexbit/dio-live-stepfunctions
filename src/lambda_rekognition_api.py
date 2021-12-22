import boto3
import json
from decimal import Decimal

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')
ddb = boto3.resource('dynamodb')

# Detecção de faces na imagem
def detect_faces(bucket, key):
    response = rekognition.detect_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response

# Detecção de rótulos na imagem
def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response

def lambda_handler(event, context):
    
    table = ddb.Table("nome_da_sua_tabela")
    
    # Obter objeto do Amazon S3
    states_input = json.dumps(event)
    get_input = json.loads(states_input)
    bucket = get_input["detail"]["requestParameters"]["bucketName"]
    key = get_input["detail"]["requestParameters"]["key"]

    try:

        # Chamada do método para reconhecimento de faces em uma imagem obtida do Amazon S3
        face_detect = detect_faces(bucket, key)
        faces_map = json.loads(json.dumps(face_detect), parse_float=Decimal)

        # Chamada do método para detecção de rótulos em uma imagem obtida do Amazon S3
        label_detect = detect_labels(bucket, key)
        labels_map = json.loads(json.dumps(label_detect), parse_float=Decimal)
        
        # Atualizar a tabela do DynamoDB com os dados obtidos do Rekognition
        table.update_item(
            Key={
                    'filename': key,
            },
            UpdateExpression='set labelData = :label, faceData = :face',
            ExpressionAttributeValues={
                ':label': labels_map,
                ':face':faces_map
            },
            ReturnValues="UPDATED_NEW"
        )

        return faces_map
    except Exception as e:
        print(e)
        raise e
