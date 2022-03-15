# Cloud Backup
Backup and archive ordinary files and folders to Google Cloud, AWS or Azure.

## Why this exists in a world with Rclone (and similar)

This script was created to solve the specific task of archiving a folder to the cloud without read access to the bucket/container and its objects.
Cloud Backup keeps an internal database of second-level files and folders which were sucessfully uploaded to the cloud.

If a file or folder changes on disk, that specific file or folder is compressed, uploaded to the cloud, and the database gets updated. What happens to the object in the bucket is invisible to the program.

## Get started
This program requires Python 3.6 or newer with PIP.

Cloud Backups supports uploading to Google Cloud Storage, Azure Blob Storage and AWS S3.

1. **Clone this repo**
```bash
git clone https://github.com/VictorWesterlund/cloud-backup
```

2. **Install dependencies**
```bash
# Install dependencies for your cloud provider "gcloud", "aws" or "azure". Leaving it empty will install everything
bash install.sh aws

# Or install everything directly with PIP
python3 -m pip install -r requirements.txt
```

3. **Copy environment variables file**
```bash
cp .env.example .env
```

4. **Edit environment variables in `.env`**
```bash
# Remember to double-slash escape paths on Windows 'E:\\path\\to\\something'

# Absolute path to folder whose contents should be backed up
SOURCE_FOLDER="/home/me/backup/"
# Name of bucket (or "container" in Azure)
TARGET_BUCKET="home_backup"

# Cloud provider. "gloud", "aws" or "azure"
SERVICE_NAME="aws"
# IAM authentication
# GCS: Path to keyfile or string (GOOGLE_APPLICATION_CREDENTIALS)
# Azure: "Connection string" from the Access Key to the container
# AWS: Access key ID and secret seperated by a ";"
SERVICE_KEY="SDJSBADYUAD;asid7sad123ebasdhasnk3dnsai"
```

5. **Run backup script**
```bash
python3 backup.py
```

Second-level files and folders should now start uploading to your destination bucket as zip archives.
Subsequent runs of the `backup.py` script will only upload changed files and folders.
In-fact; modified state is cached locally and doesn't request anything from your cloud provider.

----

You can also run `backup.py` on a schedule with CRON or equivalent for your system. No requests will be sent to the cloud unless a file or folder has actually changed

## More stuff

Here are some additional settings and commands you can try

### Back up a second-level file
```bash
python3 backup.py file 'relative/path/from/.env'
```

### Resolve CRC32 to path or vice versa
```bash
python3 resolve.py '587374759'
# output: 'hello_world.txt'

python3 resolve.py 'hello_world.txt'
# output: '587374759'
```

### Optional flags in `.env`
```bash
# The following intbool flags can be added to .env to override default behavior
# Their value in this demo is the "default" state

# Archive files and folders before uploading
COMPRESS="1"
```
