import os
#specify the directory you want to list
def print_directory_contents(path='/'):
    """
    Print all entries (files and directories) in the given directory.
    
    :param path: directory path to list (default: current directory)
    """
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error accessing {path}: {e}")
        return
# list all files
    print(f"Contents of '{path}':")
    for entry in entries:
        print(entry)

if __name__ == '__main__':
    # List contents of the current working directory
    print_directory_contents()
