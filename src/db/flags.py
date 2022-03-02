from .sqlite import SQLite

class Flags(SQLite):
    def __init__(self):
        super().__init__()

        self._columns = ["k", "v"]

    @property
    def columns(self):
        return ",".join(self._columns)

    @columns.setter
    def columns(self, columns: list):
        self._columns = columns

