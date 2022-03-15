import os
import boto3
from botocore.exceptions import ClientError

from ..fs.utils import get_file

class StorageClient:
	def __init__(self):
		self.set_access_key()
		self.client = boto3.client("s3")

		self._error = None

	@property
	def error(self):
		return self._error

	@error.setter
	def error(self, state):
		self._error = state

	# Get IAM user access key and ID
	def set_access_key(self):
		key = os.getenv("SERVICE_KEY").split(";")
		if len(key) != 2:
			self.error = "Invalid AWS service key"
			return False

		os.environ["aws_access_key_id"] = key[0]
		os.environ["aws_secret_access_key"] = key[1]

	def upload(self, path: str) -> bool:
		name = get_file(path)

		try:
			resp = self.client.upload_file(path, os.getenv("TARGET_BUCKET"), name)
		except ClientError as e:
			self.error = e
			return False
		return True