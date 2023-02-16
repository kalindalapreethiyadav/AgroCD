try:
    import zipfile
    import datetime
    import boto3
    import re
    import os
    import json
    import uuid
except Exception as e:
    pass


global AWS_ACCESS_KEY
global AWS_SECRET_KEY
global AWS_REGION_NAME
global s3bucketName

AWS_ACCESS_KEY = "XXXXXXXXXX"
AWS_SECRET_KEY = "XXXXX"
AWS_REGION_NAME = "us-east-1"
s3bucketName = "XXX"

class Datetime(object):
    @staticmethod
    def get_year_month_day():
        """
        Return Year month and day
        :return: str str str
        """
        dt = datetime.datetime.now()
        year = dt.year
        month = dt.month
        day = dt.day
        return year, month, day

class AWSS3(object):
