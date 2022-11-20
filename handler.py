# coding=utf-8

import boto3

dynamodb = boto3.resource("dynamodb")

def extractMetadata(event, context):
    print("Hello World")

def getMetadata(event, context):
    print("Hello World")

# S3 dispara evento informando Lambda que houve novo upload >> Lambda para executar as regras que você precisa, entre elas saber as dimensões da imagem 
# >> a Lambda salva no DynamoDB