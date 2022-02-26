import os
import zlib

from ..db import dbname

class FileSystem:
    def __init__(self):
        self.path = FileSystem.get_path()

    @staticmethod
    def get_path() -> str:
        return os.getenv("SOURCE_FOLDER")

    @staticmethod
    def chksum(data: str) -> str:
        return zlib.crc32(data)

    # Get metadata from candidate file or folder
    def make_obj(self, anchor: str) -> list:
        mtime = os.path.getmtime(anchor)
        if os.path.isdir(anchor):


        data = [anchor, mtime, chksum]
        return obj

    def all(self) -> list:
        content = os.listdir(self.path)
        content = list(map(self.make_obj, content))
        return content