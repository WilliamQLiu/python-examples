"""
Fabfile runs functions as commands with 'fab' then the function name

Usage:
    fab <function_name>

Examples:
    fab print_me

Assumes:
    Your environment files and variables are setup:
        e.g. AWS_DEFAULT_REGION
    And/or your ~/.aws/config and credentials file is setup with:
        config
            [default]
            region=us-west-2
        credentials
            [default]
            aws_access_key_id=''
            aws_secret_access_key=''

Example .bashrc / .bash_profile alias
    alias print_me="fab -f /home/will/GitHub/python-examples/fabric/fabfile.py print_me"
"""

import os

import boto3


AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')


def print_me():
    """ Run 'fab print_me' to test fab works locally """
    print("Hey")


def list_buckets():
    """ List all buckets in a S3 """
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print(buckets)

    response = s3_client.get_bucket_location('my_bucket')
    print(response)
    #{'LocationConstraint': 'us-west-1', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': '', ...

    return response['Buckets']


def create_bucket(bucket_name):
    """ Create a bucket """
    s3_client = boto3.client('s3')
    response = s3_client.create_bucket(Bucket=bucket_name,
                                       CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION})
    # Make sure to check that your ~/.aws/config default region is pointed to the same region as this call
    return response


def get_all_files_from_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(bucket_name)
    for s3_file in my_bucket.objects.all():
        print(s3_file.key)


def get_file_from_bucket(bucket_name, filename):
    s3_resource = boto3.resource('s3')
    response = s3_resource.Bucket('my_bucket_name').download_file('my_remote_file.txt', '/home/will/my_local_file.txt')
    print(response)


def put_file_into_bucket(bucket_name, filename):
    s3_resource = boto3.resource('s3')
    response = s3_resource.Bucket('my_bucket_name').upload_file('/home/will/my_local_file.txt', 'my_remote_file.txt')
    print(response)


if __name__ == '__main__':
    pass
