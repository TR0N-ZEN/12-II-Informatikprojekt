import os
from shutil import copy
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    source = str(pathlib.PurePath(path).joinpath(filename)) # sourcepath of current file
    destination = str(pathlib.PurePath(musicdirpath).joinpath(artist_from_filename)) # destiantion of current file according to found artists name
    if path == destination: # file is already in correct folder
        print("file already in correct folder")
        pass
    elif os.path.isdir(destination) == True: # if destinationfolder already exists
        print("destination exists")
        copy(source,destination)
        os.remove(source)
    else:
        print("destination does not exist") # if destinationfolder does not exist - create folder
        os.mkdir(destination)
        copy(source,destination)
        os.remove(source)