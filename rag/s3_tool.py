from cloud.s3_utils import generate_presigned_url

def get_image_url(s3_uri):
    key = s3_uri.replace("s3://saferide-detections/", "")
    return generate_presigned_url(key)
