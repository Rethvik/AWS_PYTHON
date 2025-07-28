import aws_session
import os
import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(format='%(asctime)s || %(levelname)s || %(name)s || %(message)s')
logger = logging.getLogger(__name__)

def generate_temporary_creditianls():
    try:
        AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
        AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
        sts_client = boto3.client('sts',
                                  aws_access_key_id=AWS_ACCESS_KEY,
                                  aws_secret_access_key=AWS_SECRET_KEY)
        response = sts_client.get_session_token(DurationSeconds=900)
        sts_client.close()
        aws_connection_init = aws_session.AwsSession(**response['Credentials'])
        aws_connection_estab = aws_connection_init.authenticate()
        s3_client = aws_connection_estab.client('s3')
        buckets = s3_client.list_buckets()
        print(f'Buckets are {buckets["Buckets"]}')
    except ClientError as e: 
        logger.exception(e)
generate_temporary_creditianls()