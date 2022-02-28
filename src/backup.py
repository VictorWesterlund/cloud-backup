import os
import importlib
from typing import Union

from . import Database, FileSystem
from . import dbname

class Backup(FileSystem):
    def __init__(self):
        super().__init__()

        self.has_change = False

        self.db = Database()
        self._cloud = None
        
        self.cloud = os.getenv("SERVICE")

    @property
    def cloud(self):
        return self._cloud

    @cloud.setter
    def cloud(self, service: str):
        CloudClient = importlib.import_module("." + service, "Client")
        self._cloud = CloudClient()

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

        # Upload to cloud
        if self.cloud.upload(item):
            # Update local database
            if self.db.set_item(item):
                print("OK")
            else:
                print("OK, BUT: Failed to update database")
        else:
            print("FAILED")
        
        return

    # Scan TARGET_FOLDER for files and folders to back up
    def backup_all(self):
        # Check all second-level files and folder at target path
        for item in self.all():
            self.backup_item(item)
        
        if not self.has_change:
            print("Up to date. No changes found")