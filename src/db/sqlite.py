import os
import pathlib
import sqlite3 as sqlite

from ..glob import file_exists

class SQLite():
    def __init__(self):
        self.db = sqlite.connect(self.get_db_path())
        self.cursor = self.db.cursor()

        # Check if the database requires configuration
        try:
            db_exists = self.query("SELECT k FROM flags WHERE k = 'INIT'")
            if not db_exists:
                self.configure_db()
        except sqlite.OperationalError:
            self.configure_db()
    
    # Strip linebreaks from pretty-printed SQL
    @staticmethod
    def format_query(sql: str) -> str: 
        return " ".join([s.strip() for s in sql.splitlines()])

    # Run SQL query
    def query(self, sql: str):
        query = self.cursor.execute(sql)
        result = query.fetchall()

        if len(result) < 1:
            return False
        
        return result

    # Get path to database file
    def get_db_path(self) -> str:
        name = ".cloudbackup.db"
        path = os.getenv("SOURCE_FOLDER")

        # Append db file name if absent
        if not path.endswith(name):
            # Append tailing slash if absent
            if path[-1] != "/":
                path += "/"
            path += name
        return path

    # Prepare a fresh db with the expected table structure
    def configure_db(self):
        cwd = str(pathlib.Path(__file__).parent.resolve())

        sql = open(cwd + "/config.sql")
        sql_str = SQLite.format_query(sql.read())

        return self.cursor.executescript(sql_str)
