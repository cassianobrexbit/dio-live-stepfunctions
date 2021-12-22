# DIO Live Step Functions - 22/12/2021

## Serviços AWS utilizados

- AWS Step Functions
- AWS Lambda
- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB
- Amazon Cloudwatch
- Amazon Cloudtrail

## Requisitos

- Conta ativa na AWS

## Roteiro de desenvolvimento

- Criar uma tabela no Amazon DynamoDB
- Criar duas funções AWS Lambda
- Criar um bucket no Amazon S3
- Criar uma máquina de estado no AWS Step Functions
- Configurar uma trail no AWS Cloudtrail
- Criar uma regra de evento no AWS Cloudwatch
- Testar

## Passos do desenvolvimento

### Criar tabela no Amazon DynamoDB

 - DynamoDB Console -> Create table - > Table name [nome_da_sua_tabela] -> Partition key [filename] -> Create table

### Criar funções lambda

#### Função de extração de metadados do arquivo no Amazon S3

 - Lambda Console -> Create function -> Author from scratch -> Function name [extract-metadata-function] -> Runtime [Python3.8] -> Role [Create new role with basic Lambda permissions] -> Create function
 - Inserir o [código](src/lambda_file_metadata.py) no editor de código -> Deploy

#### Função para chamada da API do Amazon Rekognition

- Lambda Console -> Create function -> Author from scratch -> Function name [rekognition-api-function] -> Runtime [Python3.8] -> Role [Create new role with basic Lambda permissions] -> Create function
 - Inserir o [código](src/lambda_rekognition_api.py) no editor de código -> Deploy

### Configurar políticas de acesso

- Selecionar as Roles criadas nas funções e no console do IAM criar adicionar as seguintes Policies

  - CloudWatchFullAccess
  - AmazonRekognitionFullAccess
  - AmazonS3FullAccess
  - AmazonDynamoDBFullAccess
  - AWSCloudTrail_FullAccess 

### Criar máquina de estado no AWS Step Functions

 - Step Functions Console -> State machines -> Create state machine -> Write your workflow in code -> Standard -> Inserir o [código](src/state_machine.json) no editor -> Next
 - Name [nome_da_sua_state_machine] -> Execution role [Create_new_role] -> Create state machine

### Configurar o CloudTrail

 - CloudTrail Console -> Trails -> 

