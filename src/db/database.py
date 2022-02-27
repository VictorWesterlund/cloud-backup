from .sqlite import SQLite

class Database(SQLite):
    def __init__(self):
        super().__init__()

    def item_exists(self, item: list) -> bool:
        sql = f"SELECT anchor FROM manifest WHERE anchor = '{item[0]}'"
        res = self.query(sql)

        return res

    # Test if a candidate item should be backed up
    def check_item(self, item: list) -> bool:
        sql = f"SELECT anchor, mtime, chksum FROM manifest WHERE anchor = '{item[0]}'"
        res = self.query(sql)
        if not res:
            return True

        return res

    # Insert or update item in database
    def set_item(self, item: list) -> bool:
        values = ",".join(item)
        sql = f"INSERT INTO manifest (anchor, mtime, chksum) VALUES ({values})"
        if not self.item_exists(item):
            sql = f"UPDATE manifest SET anchor = '{item[0]}', mtime = '{item[1]}', chksum = '{item[2]}' WHERE anchor = '{item[0]}'"
        res = self.query(sql)

        return res