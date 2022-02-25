import os
import sqlite3 as sqlite

from ..glob import file_exists

class SQLite():
    def __init__(self):
        self.db = sqlite.connect(self.get_db_path())
        self.cursor = self.db.cursor()

        self.init()

    def query(self, sql: str):
        result = self.cursor.execute(sql)

        if result.rowcount < 1:
            return False
        
        return result

    def get_db_path(self) -> str:
        name = ".gcsarchive.db"
        path = os.getenv("SOURCE_FOLDER")

        # Append db file name if absent
        if not path.endswith(name):
            # Append tailing slash if absent
            if path[-1] != "/":
                path += "/"
            path += name
        return path

    def configure_db(self):
        metadata_sql = "CREATE TABLE metadata (key text, value text)"
        metadata = self.query(metadata_sql)

    def init(self):
        # Set up db if it's fresh
        hasmeta_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='metadata'"
        if not self.query(hasmeta_sql):
            self.configure_db()

        return True