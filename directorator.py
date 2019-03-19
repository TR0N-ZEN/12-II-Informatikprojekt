import os
from shutil import move
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    source = str(pathlib.PurePath(path).joinpath(filename)) # sourcepath of current file
    destination = str(pathlib.PurePath(musicdirpath).joinpath(artist_from_filename)) # destiantion of current file according to found artists name
    if path == destination: # file is already in correct folder
        print("file already in correct folder")
    elif os.path.isdir(destination) == True: # if destinationfolder already exists
        print("destination exists")
        move(source,destination)
    else:
        print("destination does not exist") # if destinationfolder does not exist - create folder
        os.mkdir(destination)
        move(source,destination)