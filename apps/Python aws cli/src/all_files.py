import boto3
import os

BUCKET_NAME = 'mybucketpreek'
path = 'sub_app/sapp/'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def list_all_files():
    s3_client.list_objects_v2(
    Bucket=BUCKET_NAME,
    Prefix = path, 
)

#main function start
if __name__ == '__main__':
    print(list_all_files())