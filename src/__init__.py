from dotenv import load_dotenv
from .db import Database, dbname
from .fs import FileSystem, file_exists
from .backup import Backup

if not file_exists(".env"):
	raise FileNotFoundError("Environment variable file does not exist. Copy '.env.example' to '.env'")

load_dotenv()