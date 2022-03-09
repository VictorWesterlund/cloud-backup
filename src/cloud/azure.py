import os
from azure.storage.blob import BlobServiceClient

from ..fs.utils import get_file

class StorageClient:
	def __init__(self):
		self.client = BlobServiceClient.from_connection_string(os.getenv("SERVICE_KEY"))

		self._error = None

	@property
	def error(self):
		return self._error

	@error.setter
	def error(self, state):
		self._error = state

	def upload(self, path: str) -> bool:
		name = get_file(path)
		blob = self.client.get_blob_client(container=os.getenv("TARGET_BUCKET"), blob=name)

		try:
			with open(path, "rb") as f:
				blob.upload_blob(f,overwrite=True)
			return True
		except Exception as e:
			if e.response.status_code == 403:
				self.error = "Azure: Access key invalid or lacking required permissions"
			return False