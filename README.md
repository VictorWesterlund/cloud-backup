# Cloud Backup
Backup and archive ordinary files and folders to Google Cloud, AWS or Azure.

## Get started
This program requires Python 3.6 or newer with PIP.

1. **Clone this repo**
```
git clone https://github.com/VictorWesterlund/cloud-backup
```

2. **Install dependencies**
```
python3 -m pip install -r requirements.txt
```

3. **Copy environment variables file**
```
cp .env.example .env
```

4. **Edit environment variables**
Open `.env` with your text editor of choice and fill out these required variables
```bash
# Path to the local folder to back up
SOURCE_FOLDER=
# Name of the remote bucket (destination)
TARGET_BUCKET=

# Cloud provider (gcs, s3, azure)
SERVICE_NAME=
# Path to service account key file
SERVICE_KEY=
```

5. **Run backup script**
```
python3 backup.py
```

Second-level files and folders should now start uploading to your destination bucket as zip archives.
Subsequent runs of the `backup.py` script will only upload changed files and folders.
In-fact; modified state is cached locally and doesn't request anything from your cloud provider.
