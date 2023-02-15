import boto3
import os

BUCKET_NAME = 'mybucketpreek'
Object_File_Name = 'sub_app/helm-charts-main.gz.zip'
Local_file_Name = 'download.zip'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def downlaod_file():
    #file_path = os.path.dirname(__file__) + 'sub_app/helm-charts-main.gz.zip'
    return s3_client().download_file(BUCKET_NAME, Object_File_Name, Local_file_Name)

#main function start
if __name__ == '__main__':
    print(downlaod_file())