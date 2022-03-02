import os
from google.cloud import storage

from ..fs.utils import get_file

# Client for Google Cloud Storage
class StorageClient:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("SERVICE_KEY")

        client = storage.Client()
        self.bucket = client.bucket(self.get_bucket())

    def get_bucket(self):
        return os.getenv("TARGET_BUCKET")

    def upload(self, path: str) -> bool:
        name = get_file(path)
        blob = self.bucket.blob(name)

        try:
            with open(path, "rb") as f:
                blob.upload_from_file(f)
            return True
        except:
            return False