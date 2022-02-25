import os.path

def file_exists(file: str) -> bool:
    return os.path.isfile(file)