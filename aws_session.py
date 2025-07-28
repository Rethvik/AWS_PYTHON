import boto3
from botocore.exceptions import ClientError
import logging


logger = logging.getLogger(__name__)
class AwsSession:
    def __init__(self,AccessKeyId,SecretAccessKey,SessionToken,Expiration):
        self._aws_access_key = AccessKeyId
        self._aws_secret_key = SecretAccessKey
        self._aws_session_token = SessionToken
        self._expiration = Expiration
    def authenticate(self):
        try:
            session = boto3.Session(
                aws_access_key_id=self._aws_access_key,
                aws_secret_access_key=self._aws_secret_key,
                aws_session_token=self._aws_session_token)
            return session
        except ClientError as e:
            logger.error(e)
        except Exception as e:
            logger.exception(e)