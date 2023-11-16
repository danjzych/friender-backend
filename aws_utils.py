import boto3
import os
from dotenv import load_dotenv
import boto3.session

load_dotenv()
aws_access_key = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = os.environ['IMAGE_BUCKET']


# Below is needed for pre-signed URLs: signature version must be updated,
# Region name is a hacky workaround to an error I was getting.

session = boto3.session.Session(region_name='us-east-2')
s3 = session.client(
    's3', config=boto3.session.Config(signature_version='s3v4'))


# Generate pre-signed URL for image already in bucket
def get_image_url(img_name):
    signed_url = s3.generate_presigned_url("get_object",
                                           Params={
                                               "Bucket": bucket_name, "Key": img_name},
                                           ExpiresIn=3600)
    return signed_url


def upload_image(filepath, img_filename):
    s3.upload_file(filepath, bucket_name, img_filename)
    return "upload complete"
