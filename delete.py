import json
import logging

import boto3

from LambdaResponse import LambdaResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('Student')


def delete(event, context):
    logger.info('got event{}'.format(event))
    logger.info('context{}'.format(context))
    body = json.loads(event['body'])
    data = body['data']
    logger.info('data = {}'.format(data))
    table.delete_item(
        Key={
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
    )
    response = LambdaResponse('false', 200, event['headers'], '{"messages" : "SUCCESS"}')
    return vars(response)
