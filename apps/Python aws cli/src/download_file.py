import boto3
import os

BUCKET_NAME = 'mybucketpreek'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def downlaod_small_file():
    file_path = os.path.dirname(__file__) + 'sub_app/helm-charts-main.gz.zip'
    return s3_client().download_file(file_path, BUCKET_NAME, 'sub_app/helm-charts-main.gz.zip')

#main function start
if __name__ == '__main__':
    print(downlaod_small_file())