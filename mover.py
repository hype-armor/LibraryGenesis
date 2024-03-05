import os

from sympy import true
def delete(path):
    for path, directories, files in os.walk(path):
        for file in files:
            print(path + '\\' + file)
            os.remove(path + '\\' + file)
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
    tree = '\\'.join(destination.split('\\')[:-1])
    print(f'creating {tree}')
    create_missing_dirs(tree)
    os.rename(source, destination)
    