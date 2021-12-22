import json
import boto3
import uuid

s3 = boto3.client('s3')
ddb = boto3.resource('dynamodb')

# Função para extração de metadados de arquivo enviado ao Amazon S3
def lambda_handler(event,context):
    table = ddb.Table("nome_da_sua_tabela")
    
    # Leitura da entrada da máquina de estado (state machine)
    states_input = json.dumps(event)
    get_bucket_values = json.loads(states_input)

    try:

        bucket = get_bucket_values["detail"]["requestParameters"]["bucketName"]
        key = get_bucket_values["detail"]["requestParameters"]["key"]
        
        # Chamada do bucket S3
        obj = s3.get_object(Bucket=bucket, Key=key)
        newData = {
            'id': str(uuid.uuid4().hex),
            'bucket':  bucket,
            'filename': key,
            'filesize': int(obj['ContentLength']),
            'contentType': obj['ContentType'],
            'labelData':{},
            'faceData':{},
            }

        # Inserir dados no DynamoDB
        table.put_item(Item=newData)
        
        return newData
        
    except Exception as e:

        raise e
