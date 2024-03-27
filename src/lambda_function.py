import os
import awsgi
import boto3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return ("Hello Flask!")

def lambda_handler(event, context):
    # https://github.com/slank/awsgi/issues/73#issuecomment-1986868661
    event['httpMethod'] = event['requestContext']['http']['method']
    event['path'] = event['requestContext']['http']['path']
    event['queryStringParameters'] = event.get('queryStringParameters', {})
    return awsgi.response(app, event, context) 