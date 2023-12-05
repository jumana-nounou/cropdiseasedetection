import os

def count_folders(path):
    return len([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])