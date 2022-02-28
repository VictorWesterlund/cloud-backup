import os
import zlib

from ..db import dbname

class FileSystem:
    def __init__(self):
        self.path = FileSystem.get_path()

    @staticmethod
    def get_path() -> str:
        return os.getenv("SOURCE_FOLDER")

    # Calculate a CRC32 checksum of provided data
    @staticmethod
    def chksum(data: str) -> str:
        encoded = data.encode("utf-8")
        return zlib.crc32(encoded)

    # Get metadata from candidate file or folder
    def get_item(self, path: str) -> tuple:
        # Ignore SQLite temp files
        if path.endswith(".db-journal"):
            return False
        
        mtime = os.path.getmtime(path)
        chksum = FileSystem.chksum(path + str(mtime))

        data = (path, chksum)
        return data

    # Get all second-level files and folders for path
    def all(self) -> list:
        content = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        items = []

        for item in content:
            data = self.get_item(item)
            if data:
                items.append(data)

        return items