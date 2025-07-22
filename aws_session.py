import boto3
from botocore.exceptions import ClientError

class AwsSession:
    def __init__(self,aws_access_key,aws_secret_key):
        self._aws_access_key = aws_access_key
        self._aws_secret_key = aws_secret_key
    def authenticate(self):
        try:
            session = boto3.Session(aws_access_key_id=self._aws_access_key,aws_secret_access_key=self._aws_secret_key)
            return session
        except ClientError as e:
            print(e)