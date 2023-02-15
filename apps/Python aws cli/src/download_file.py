import boto3
import os

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def downlaod_file():
    #file_path = os.path.dirname(__file__) + 'sub_app/helm-charts-main.gz.zip'
    return s3_client().download_file('mybucketpreek', 'sub_app/sapp/helm-v3.11.1-linux-ppc64le.tar.gz.asc','helm-v3.11.1-linux-ppc64le.tar.gz.asc')

#main function start
if __name__ == '__main__':
    print(downlaod_file())