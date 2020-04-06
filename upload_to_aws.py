#!/usr/bin/env python3

#imports

import boto3
from botocore.exceptions import NoCredentialsError
import configparser

config = configparser.ConfigParser()
config.read('dl.cfg')


ACCESS_KEY = config['AWS']['AWS_ACCESS_KEY_ID']
SECRET_KEY = config['AWS']['AWS_SECRET_ACCESS_KEY']
local_file = config['FILES']['LOCAL_FILE']
bucket_name =  config['S3']['BUCKET_NAME']
s3_file = config['FILES']['S3_FILE']



# Task 1. upload local file to S3 bucket
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws(local_file, bucket_name, s3_file_name)
