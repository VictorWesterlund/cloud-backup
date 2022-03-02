import os
from typing import Union

from .sqlite import SQLite

class Database(SQLite):
    def __init__(self):
        super().__init__()

        self._columns = ["anchor", "chksum"]

    @property
    def columns(self):
        return ",".join(self._columns)

    @columns.setter
    def columns(self, columns: list):
        self._columns = columns

    # Create SQL string CSV from list
    @staticmethod
    def str_csv(items: Union[list, tuple]) -> str:
        items = list(map(lambda value : f"'{str(value)}'", items))
        items = ",".join(items)

        return items

    # Check if item exists in the database
    def item_exists(self, item: Union[list, tuple]) -> bool:
        sql = f"SELECT anchor FROM manifest WHERE anchor = '{item[0]}'"
        res = self.query(sql)

        return res

    # Check if item should be backed up by comparing mtime and checksum
    def check_item(self, item: Union[list, tuple]) -> bool:
        sql = f"SELECT {self.columns} FROM manifest WHERE anchor = '{item[0]}'"
        db_item = self.query(sql)

        # New item or item changed, so back it up
        if not db_item or (item != db_item[0]):
            return True
        return False

    # Insert or update item in database
    def set_item(self, item: Union[list, tuple]) -> bool:
        sql = f"UPDATE manifest SET anchor = '{item[0]}', chksum = {item[1]} WHERE anchor = '{item[0]}'"

        if not self.item_exists(item):
            sql = f"INSERT INTO manifest ({self.columns}) VALUES ('{item[0]}', {item[1]})"
        self.query(sql)

        return True