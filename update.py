import logging

import boto3
import simplejson as json

from LambdaResponse import LambdaResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('Student')


def update(event, context):
    logger.info('got event{}'.format(event))
    logger.info('context{}'.format(context))
    logger.info('body{}'.format(event['body']))
    body = json.loads(event['body'])
    data = body['data']
    logger.info('data = {}'.format(data))
    table.update_item(
        Key={
            'first_name': data['first_name'],
            'last_name': data['last_name']
        },
        UpdateExpression='SET year_in = :val1',
        ExpressionAttributeValues={
            ':val1': data['year_in']
        }
    )
    response = table.get_item(
        Key={
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
    )
    item = response['Item']
    logger.info("item = {}".format(item))
    response = LambdaResponse('false', '200', event['headers'], json.dumps(item))
    return vars(response)
