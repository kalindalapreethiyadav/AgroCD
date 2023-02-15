import boto3

BUCKET_NAME = 'mybucketpreek'
path = 'sub_app/sapp/'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def filter_charts_file():
    paginator = s3_client.get_paginator('list_objects')
    result = paginator.paginate(Bucket='mybucketpreek', Delimiter='/')
    for prefix in result.search('helm'):
        print(prefix.get('Prefix'))

    
if __name__ == '__main__':
    print(filter_charts_file())