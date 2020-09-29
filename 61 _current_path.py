import os

def current_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    return dir_path


print(current_path())
