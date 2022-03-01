import os
import importlib

# This class initializes only the module for the requested service.
# It sits as an intermediate between the initiator script and client library.
class Storage:
    def __init__(self):
        self._service = None
        self.service = os.getenv("PROVIDER_NAME")

    @property
    def service(self):
        return self._service

    # Create a new storage client for the requested service
    @service.setter
    def service(self, service: str):
        if not service:
            service = "gcs"
        module = importlib.import_module("src.cloud." + service)

        self._service = module.StorageClient(os.getenv("TARGET_BUCKET"))

    @staticmethod
    def get_args(values):
        values.pop(-1)
        return values

    def upload(self, *argv):
        return self.service.upload(*argv)