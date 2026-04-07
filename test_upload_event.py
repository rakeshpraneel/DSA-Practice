import importlib.util
import json
from pathlib import Path

import boto3
from botocore.stub import Stubber


def load_lambda_module():
    """Load lambda-s3-flow.py as a module named lambda_s3_flow."""
    file_path = Path(__file__).with_name("lambda-s3-flow.py")
    spec = importlib.util.spec_from_file_location("lambda_s3_flow", file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)  # type: ignore[arg-type]
    return module


def main() -> None:
    lambda_mod = load_lambda_module()
    upload_event = lambda_mod.upload_event

    bucket_name = "test-bucket"
    key = "events/test.json"
    event = {"event": {"message": "hello from test", "id": 123}}

    s3 = boto3.client("s3", region_name="us-east-1")
    stubber = Stubber(s3)

    expected_body = json.dumps(event["event"])

    stubber.add_response(
        "put_object",
        service_response={},
        expected_params={
            "Bucket": bucket_name,
            "Key": key,
            "Body": expected_body,
            "ContentType": "application/json",
        },
    )

    with stubber:
        # Monkeypatch boto3.client to return our stubbed client when S3 is requested
        original_client = boto3.client

        def fake_client(service_name, *args, **kwargs):
            if service_name == "s3":
                return s3
            return original_client(service_name, *args, **kwargs)

        boto3.client = fake_client  # type: ignore[assignment]
        try:
            upload_event(event, bucket_name, key)
            print("upload_event called successfully with stubbed S3.")
            print("Bucket:", bucket_name)
            print("Key:", key)
            print("Body:", expected_body)
        finally:
            boto3.client = original_client  # type: ignore[assignment]


if __name__ == "__main__":
    main()

