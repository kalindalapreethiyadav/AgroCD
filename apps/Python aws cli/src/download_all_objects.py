import boto3
import os

BUCKET_NAME = 'mybucketpreek'
Path = 'sub_app/sapp/'
#Object_File_Name = 'sub_app/helm-charts-main.gz.zip'
#Local_file_Name = 'download.zip'

# download files that are in a sub-folder in an S3 bucket.
def download_all_objects_in_folder():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(BUCKET_NAME)
    objects = my_bucket.objects.filter(Prefix='sub_app/sapp/')
    for obj in objects:
        Path, filename = os.path.split(obj.key)
        my_bucket.download_file(obj.key, filename)

#main function start
if __name__ == '__main__':
    print(download_all_objects_in_folder())