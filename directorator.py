import os
from shutil import copy2
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    source = path + filename # sourcepath of current file
    destination = musicdirpath + artist_from_filename + "\\" # destiantion of current file according to found artists name
    print(source + "\n" + destination )
    if path == destination: # file is already in correct folder
        print("file already in correct folder")
        pass
    elif os.path.isdir(destination) == True: # if destinationfolder already exists
        print("destination exists")
        copy2(source,destination)
        os.remove(source)
    else:
        print("destination does not exist") # if destinationfolder does not exist - create folder
        os.mkdir(destination)
        copy2(source,destination)
        os.remove(source)