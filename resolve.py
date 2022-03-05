import sys

from src import Database

class Resolve(Database):
	def __init__(self):
		super().__init__()

		if self.item_exists(sys.argv[1]):
			self.path_to_chksum()
		else:
			self.chksum_to_path()

	def path_to_chksum(self):
		print("Something")

	def chksum_to_path(self):
		print("Something else")

if len(sys.argv) > 2:
	Resolve()
else:
	print("Invalid argument length: Need at least two")