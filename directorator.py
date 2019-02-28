import os
from shutil import copy
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    source = str(pathlib.PurePath(path).joinpath(filename))
    destination = str(pathlib.PurePath(musicdirpath).joinpath(artist_from_filename))
    if path == destination:
        print("file already in correct folder")
        pass
    elif os.path.isdir(destination) == True:
        print("destination exists")
        copy(source,destination)
        os.remove(source)
    else:
        print("destination does not exist")
        os.mkdir(destination)
        copy(source,destination)
        os.remove(source)