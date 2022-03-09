import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Union

from .cloud import Storage as StorageClient
from . import Database, FileSystem
from . import dbname

class Backup(FileSystem):
    def __init__(self):
        super().__init__()
        self.enable_logging()

        self.has_change = False

        self.db = Database()
        self.cloud = StorageClient()

        self.compress = self.db.get_flag("COMPRESS")

    # Configure logging
    def enable_logging(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Start console logging")
        log_format = logging.Formatter("[%(asctime)s][%(levelname)s]: %(name)s: %(message)s")

        # Log to console
        log_console = logging.StreamHandler()
        log_console.setLevel(logging.INFO)
        log_console.setFormatter(log_format)

        self.log.addHandler(log_console)

        # Log to file
        log_file_path = os.getenv("LOG_FILE")
        if log_file_path:
            self.log.debug("Start file logging")
            log_file = RotatingFileHandler(
                log_file_path,
                mode        = "a",
                maxBytes    = 50 * 1024 * 1024,
                backupCount = 5,
                encoding    = None,
                delay       = False
            )

            log_file.setLevel(os.getenv("LOG_LEVEL"))
            log_file.setFormatter(log_format)

            self.log.addHandler(log_file)

    # Backup a file or folder
    def backup_item(self, item: Union[list, str], silent: bool = True) -> bool:
        if isinstance(item, str):
            item = self.get_item(item)

        # Check item against db if it has changed
        db_resp = self.db.check_item(item)
        if not db_resp:
            return

        # Back up changes to database in silence
        if item[0].endswith(dbname):
            self.db.set_item(item)
            return

        self.has_change = True

        self.log.info(f"'{item[0]}': Uploading")
        print(f"⏳ | Uploading: '{item[0]}'", end="\r")

        blob = item
        # Upload as zip archive
        if self.compress:
            self.log.debug(f"'{item[0]}': Compressing")
            blob = FileSystem.zip(blob)

        # Upload to cloud
        if self.cloud.upload(blob):
            self.log.debug(f"'{item[0]}': Uploaded")
            print(f"✅ | Upload successful: '{item[0]}'")
            # Update local database
            if not self.db.set_item(item):
                self.log.warn(f"'{item[0]}': Failed to update database")
                print("⚠️ | Failed to update database")
        else:
            self.log.error(f"'{item[0]}': {self.cloud.error}")
            print(f"❌ | Upload failed: '{item[0]}'")

        # Remove temp zip
        if self.compress:
            FileSystem.delete(blob)

        # Deprecated: Run when a single item is backed up directly
        if not silent and not self.has_change:
            self.log.info("No changes found")
            print("✅ | Up to date. No changes found")
        
        return

    # Scan TARGET_FOLDER for files and folders to back up
    def backup_all(self):
        # Check all second-level files and folder at target path
        for item in self.all():
            self.backup_item(item)
        
        if not self.has_change:
            self.log.info("No changes found")
            print("✅ | Up to date. No changes found")