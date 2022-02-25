from dotenv import load_dotenv

from .glob import file_exists
from .db import Database
from .gcs import StorageClient

if not file_exists(".env"):
	raise FileNotFoundError("Environment variable file does not exist. Copy '.env.example' to '.env'")

load_dotenv()