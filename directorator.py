import os
from shutil import copy
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    source = pathlib.PurePath(path).joinpath(filename)
    print(source)
    destination = pathlib.PurePath(musicdirpath).joinpath(artist_from_filename)
    print(destination)
    if os.path.isdir(destination) == True:
        print("destination exists")
        copy(source,destination)
    else:
        print("destination does not exist")
        os.mkdir(destination)
        # copy(source,destination)
    os.remove(source)