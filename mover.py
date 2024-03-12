import os

SLASHES = '/'
if os.name == 'nt':
    SLASHES = '\\'
    
def translate_dir(path):
    new_path = path
    if os.name == 'nt':
        new_path = new_path.replace("/downloads/", "P:\\media\\").replace('/', '\\')
    return new_path

def delete(path):
    path = translate_dir(path)
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
    path = translate_dir(path)
    os.makedirs(path, exist_ok=True)

def move(source, destination):
    source = translate_dir(source)
    destination = translate_dir(destination)
    print(f'removing {destination}')
    delete(destination)
    tree = SLASHES.join(destination.split(SLASHES)[:-1])
    print(f'creating {tree}')
    create_missing_dirs(tree)
    os.rename(source, destination)