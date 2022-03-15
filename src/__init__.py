import os
from dotenv import load_dotenv

from .db import Database, dbname
from .fs import FileSystem, file_exists
from .backup import Backup

# Required environment variables
required_vars = (
	"SOURCE_FOLDER",
	"TARGET_BUCKET",
	"SERVICE_NAME",
	"SERVICE_KEY",
	"LOG_LEVEL"
)

if not file_exists(".env"):
	raise FileNotFoundError("Environment variable file does not exist. Copy '.env.example' to '.env'")

load_dotenv()

# Check that required environment variables are set
if not all(map(lambda var: os.getenv(var), required_vars)):
	raise SystemExit("One or more required environment variables in '.env' have not been set")