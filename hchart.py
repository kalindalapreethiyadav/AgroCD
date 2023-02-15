#!/usr/bin/python
import boto3

BUCKET_NAME = "mybucketpreek"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'helm-charts-main.zip')
s3_object.download_file('downloaded.pdf')
print("File has been downloaded")

#listing the bucket files
s3_bucket = s3_resource.Bucket(BUCKET_NAME)
print("Listing Bucket Files or Objects")
for obj in s3_bucket.objects.all():
    print(obj.key)