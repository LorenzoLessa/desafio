import json
import pprint
import urllib.parse
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def extractMetadata(event, context):
    s3 = boto3.resource('s3')
    dynamodb = boto3.resource('dynamodb')

    # Recuperar o nome do bucket do payload. 
    bucket = event['Records'][0]['s3']['bucket']['name']
    # Recuperar nome do arquivo do payload. 
    nomearquivo = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:

        #Buscar o arquivo do bucket.
        arquivo = s3.get_Object(Bucket=bucket, Key=nomearquivo)
        # Desserializar o conteúdo do arquivo.
        texto = arquivo['Body'].read().decode()
        dados = json.loads(texto)

        # Print do conteúdo do arquivo.
        # print(dados)

        # Iteração para selecionar as colunas e gravar os dados no DynamoDB.
        for dado in dados:
            tabela = dynamodb.Table('dados-de-imagens-do-s3bucket')
            tabela.put_item(Item={
                'x-amz-meta-1': dado['dimensões'],  
                'x-amz-meta-2': dado['tamanho-do-arquivo'],
            })

    except Exception as e:
        print(e)
        print(f'Error getting object {nomearquivo} from bucket {bucket}.')
        raise e

# Retorna os metadados armazenados no DynamoDB.
def getMetadata(s3objectkey):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('dados-de-imagens-do-s3bucket')
    print(table.item_count)

# Faz download da imagem do s3.
def getImage(s3objectkey):
    try:
        s3 = boto3.client('s3')
        s3.download_file('project.com-lorenzolessa', s3objectkey, 'arquivobaixado.jpg')

    except ClientError as e:
        print(e)  

# Pesquisa os metadados salvos no DynamoDB.
def infoImages():
    # Qual é a imagem que contém o maior tamanho?
    # Qual é a imagem que contém o menor tamanho?
    # Quais os tipos de imagem salvas no S3?
    # Qual a quantidade de cada tipo de imagem salva?
    pass

# Criei está função para verificar se os objetos dentro do bucket eram condizentes com os que coloquei.
def listaObjetos(bucket_name):
    try:
        s3_client = boto3.resource('s3')
        bucket = s3_client.Bucket(bucket_name)

        for obj in bucket.objects.all():
            pprint.pprint(obj.key)

    except ClientError as e:
        print(e)

listaObjetos("project.com-lorenzolessa")
getImage('solvimm_logo.jpg')