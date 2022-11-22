import json
import urllib.parse
import boto3

def extractMetadata(event, context):
    s3 = boto3.resource('s3')
    dynamodb = boto3.resource('dynamodb')

    # Recuperar o nome do bucket do payload 
    bucket = event['Records'][0]['s3']['bucket']['name']
    # Recuperar nome do arquivo do payload 
    nomearquivo = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:

        #Buscar o arquivo do bucket
        arquivo = s3.get_Object(Bucket=bucket, Key=nomearquivo)
        # Desserializar o conteúdo do arquivo
        texto = arquivo['Body'].read().decode()
        dados = json.loads(texto)

        # Print do conteúdo do arquivo
        # print(dados)

        # Iteração para selecionar as colunas e gravar os dados no DynamoDB 
        for registros in dados:

    except Exception as e:
        print(e)
        print(f'Error getting object {nomearquivo} from bucket {bucket}.')
        raise e

def getMetadata(event, context):
    pass

def getImage(s3objectkey):
    pass
    # Faz download da imagem do s3

def infoImages():
    pass
    # ● Qual é a imagem que contém o maior tamanho?
    # ● Qual é a imagem que contém o menor tamanho?
    # ● Quais os tipos de imagem salvas no S3?
    # ● Qual a quantidade de cada tipo de imagem salva?

# S3 dispara evento informando Lambda que houve novo upload >> Lambda para executar as regras que você precisa, entre elas saber as dimensões da imagem 
# >> a Lambda salva no DynamoDB
