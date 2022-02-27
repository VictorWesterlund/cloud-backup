from typing import Union

from . import Database, FileSystem

class Backup(FileSystem):
    def __init__(self):
        super().__init__()
        self.db = Database()

    def backup_item(self, item: Union[list, str]) -> bool:
        if isinstance(item, str):
            item = self.get_item(item)

        # Check item against db if it has changed
        db_resp = self.db.check_item(item)
        if not db_resp:
            return True

        self.db.set_item(item)
        
        return True

    def backup_all(self):
        for item in self.all():
            self.backup_item(item)