import sys

from src import Backup, file_exists

# Back up a single file by path
def file_backup():
	path = sys.argv[2]

	if len(sys.argv) < 3:
		return print("Invalid argument length: Expected path to file or folder")
	
	if not file_exists(path):
		return print(f"File or folder at '{path}' does not exist")

	return Backup().backup_item(path, False)

def run(method):
	methods = {
		"file": file_backup,
		"all" : Backup().backup_all
	}

	if method not in methods:
		return print(f"Invalid argument '{method}'")

	return methods[method]()

if len(sys.argv) > 1:
	run(sys.argv[1])
else:
	run("all")