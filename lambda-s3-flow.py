import json

import boto3

def upload_event(event, bucket_name, key):
    s3 = boto3.client("s3")

    content = event.get("event",{})
    json_dump = json.dumps(content)

    s3.put_object(
        Bucket= bucket_name,
        Key=key,
        Body=json_dump,
        ContentType="application/json"
    )