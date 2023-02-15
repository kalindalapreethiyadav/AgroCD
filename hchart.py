import boto3
import json
import os
import threading
import sys

from boto3.s3.transfer import TransferConfig

BUCKET_NAME = 'niyazi-s3-2018-bucket'



def list_buckets():
    return s3_client().list_buckets()

