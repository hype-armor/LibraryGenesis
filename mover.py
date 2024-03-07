import os

SLASHES = '/'
if os.name == 'nt':
    SLASHES = '\\'

def delete(path):
    for path, directories, files in os.walk(path):
        for file in files:
            print(path + SLASHES + file)
            os.remove(path + SLASHES + file)
        for directory in directories:
            print(directory)
            delete(directory)
            os.rmdir(dir)
    if os.path.isdir(path):
        os.rmdir(path)
        
def create_missing_dirs(path):
    os.makedirs(path, exist_ok=True)

def move(source, destination):
    print(f'removing {destination}')
    delete(destination)
    tree = SLASHES.join(destination.split(SLASHES)[:-1])
    print(f'creating {tree}')
    create_missing_dirs(tree)
    os.rename(source, destination)
    