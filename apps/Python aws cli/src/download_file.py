import boto3
import boto3.session

BUCKET_NAME = 'mybucketpreek'

s3_resource = boto3.resource('s3')
bucket_obj = s3_resource.Bucket(BUCKET_NAME)
for obj in bucket_obj.objects.all():
        print(obj.key)








'''

my_bucket = 'mybucketpreek'

def s3_client():
    s3 = boto3.client('s3')
    return s3

def downlaod_file():
    #file_path = os.path.dirname(__file__) + 'sub_app/helm-charts-main.gz.zip'
    return s3_client().download_file('mybucketpreek', 'sub_app/sapp/helm-v3.11.1-linux-ppc64le.tar.gz.asc','helm-v3.11.1-linux-ppc64le.tar.gz.asc')


    '''