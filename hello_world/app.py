import json

import boto3

instances = None
client = None

def hello(event, context):
    global client
    if client is None:
        client = boto3.client('servicediscovery')
    instances = client.discover_instances(
        NamespaceName='sls.willy.works',
        ServiceName='example-stream',
        QueryParameters={
            'env': 'prod'
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            'stream_name': instances['Instances'][0]['InstanceId'],
        })
    }


def world(event, context):
    global client
    global instances
    if instances is None:
        if client is None:
            client = boto3.client('servicediscovery')
        instances = client.discover_instances(
            NamespaceName='sls.willy.works',
            ServiceName='example-stream',
            QueryParameters={
                'env': 'prod'
            }
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            'stream_name': instances['Instances'][0]['InstanceId'],
        })
    }
