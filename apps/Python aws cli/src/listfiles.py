import boto3

BUCKET_NAME = 'mybucketpreek'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3
'''
def s3_resource():
    s3 = boto3.resource('s3')
    return s3
'''

#creating function to list buckets
def list_buckets():
    return s3_client().list_buckets()

#main function start
if __name__ == '__main__':
    print(list_buckets())