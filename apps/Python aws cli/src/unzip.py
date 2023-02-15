import boto3

BUCKET_NAME = 'preek-helmcharts'
OBJECT_NAME = ''
FILE_NAME = ''

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def s3_unzipobject():
    return s3_client.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

#main function start
if __name__ == '__main__':
    print(s3_unzipobject())