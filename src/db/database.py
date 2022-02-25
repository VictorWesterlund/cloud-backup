from .sqlite import SQLite

class Database(SQLite):
    def __init__(self):
        super().__init__()

    def backup_candidate(self, anchor: str) -> bool:
        sql = f"SELECT anchor, mtime, chksum FROM manifest WHERE anchor = '{anchor}'"
        data = self.query(sql)

        return True