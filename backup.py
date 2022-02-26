import sys
from src import Database, FileSystem

class Backup(FileSystem):
    def __init__(self, argv):
        super().__init__()
        self.db = Database()

    def backup(self, obj: list) -> bool:
        db_response = self.db.check_obj(obj)
        return True

    def backup_all(self):
        for item in self.all():
            self.backup(item)

Backup(sys.argv).backup_all()
print("OK")