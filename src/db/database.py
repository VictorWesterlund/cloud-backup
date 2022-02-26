from .sqlite import SQLite

class Database(SQLite):
    def __init__(self):
        super().__init__()

    # Test if a candidate item should be backed up
    def check_item(self, obj: list) -> bool:
        sql = f"SELECT anchor, mtime, chksum FROM manifest WHERE anchor = '{obj.anchor}'"
        data = self.query(sql)

        return True