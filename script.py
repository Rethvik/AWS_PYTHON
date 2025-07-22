import aws_session
import os
def run():
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    local_session = aws_session.AwsSession(AWS_ACCESS_KEY,AWS_SECRET_KEY)
    aws_connection = local_session.authenticate()
    s3_client = aws_connection.client('s3')
    data = s3_client.list_buckets()
    print(f'Buckets are {data["Buckets"]}')
run()