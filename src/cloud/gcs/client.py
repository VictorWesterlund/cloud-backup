import os
from os.path import exists
from google.cloud import storage

class StorageClient(storage.Client):
    def __init__(self, bucket: str = None):
        if not bucket:
            bucket = os.getenv("TARGET_BUCKET")
        
        if not self.gcloud_key_exists():
            raise Exception("GOOGLE_APPLICATION_CREDENTIALS has to point to a key file")

        super().__init__()

    # Check if env var is set to a key file
    def gcloud_key_exists(self) -> bool:
        keyfile = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        if not keyfile or not exists(keyfile):
            return False
        return True