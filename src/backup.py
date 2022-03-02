from typing import Union

from .cloud import Storage as StorageClient
from . import Database, FileSystem
from . import dbname

class Backup(FileSystem):
    def __init__(self):
        super().__init__()

        self.has_change = False

        self.db = Database()
        self.cloud = StorageClient()

        self.compress = self.db.get_flag("COMPRESS")

    # Backup a file or folder
    def backup_item(self, item: Union[list, str]) -> bool:
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

        print(f"Uploading: '{item[0]}' ... ", end="")

        blob = item
        # Upload as zip archive
        if self.compress:
            blob = FileSystem.zip(blob)

        # Upload to cloud
        if self.cloud.upload(blob):
            # Update local database
            if self.db.set_item(item):
                print("OK")
            else:
                print("OK, but failed to update database")
        else:
            print("FAILED")

        # Remove temp zip
        if self.compress:
            FileSystem.delete(blob)
        return

    # Scan TARGET_FOLDER for files and folders to back up
    def backup_all(self):
        # Check all second-level files and folder at target path
        for item in self.all():
            self.backup_item(item)
        
        if not self.has_change:
            print("Up to date. No changes found")