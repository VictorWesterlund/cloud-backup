import os.path
import ntpath

# Check if a file exists
def file_exists(file: str) -> bool:
    return os.path.isfile(file)

# Get parent directory of file
def get_parent(path: str) -> str:
    return os.path.dirname(path)

# Get filename from path string
def get_file(path: str) -> str:
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)