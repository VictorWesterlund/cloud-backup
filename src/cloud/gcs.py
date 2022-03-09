import os
from google.cloud import storage

from ..fs.utils import get_file

# Client for Google Cloud Storage
class StorageClient:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("SERVICE_KEY")

        client = storage.Client()
        self.bucket = client.bucket(self.get_bucket())

        self._error = None

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, state):
        self._error = state

    def get_bucket(self):
        return os.getenv("TARGET_BUCKET")

    def upload(self, path: str) -> bool:
        self.error = None
        name = get_file(path)
        blob = self.bucket.blob(name)

        try:
            with open(path, "rb") as f:
                blob.upload_from_file(f)
            return True
        except Exception as e:
            if e.response.status_code == 403:
                self.error = "GCS: Forbidden: Account lacks 'storage.objects.create' role on target bucket"
            return False