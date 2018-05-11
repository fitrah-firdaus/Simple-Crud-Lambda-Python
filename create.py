import json
import logging
import uuid

import boto3

from LambdaResponse import LambdaResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('Student')


def create(event, context):
    logger.info('got event{}'.format(event))
    logger.info('context{}'.format(context))
    body = event['body']
    logger.info('body{}'.format(body))
    data = json.loads(body)
    for i, it in enumerate(data['data']):
        table.put_item(
            Item={
                'id': str(uuid.uuid1()),
                'first_name': it['first_name'],
                'last_name': it['last_name'],
                'year_in': it['year_in'],
                'subject': it['subject']
            }
        )
    body = '{"row":' + str(i + 1) + '}'
    response = LambdaResponse('false', 200, event['headers'], body)
    return vars(response)
#    return body
