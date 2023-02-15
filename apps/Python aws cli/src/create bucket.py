import boto3

BUCKET_NAME = 'preek-helmcharts'

def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

def s3_resource():
    s3 = boto3.resource('s3')
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
    )



if __name__ == '__main__':
    print(create_bucket(BUCKET_NAME))