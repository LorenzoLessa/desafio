# coding=utf-8

import boto3

s3 = boto3.resource('s3')
#dynamodb = boto3.resource("dynamodb")


print('Existing buckets:')
for bucket in s3.buckets.all():
    print(bucket.name)

def extractMetadata(event, context):
    pass

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