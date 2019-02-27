import os
from shutil import copyfile
import pathlib

def directorator(musicdirpath,filename,path,artist_from_filename):
    target = pathlib.PurePath(path).joinpath(filename)
    destination = pathlib.PurePath(musicdirpath).joinpath(artist_from_filename)
    if os.path.isdir(destination) == True:
        copyfile(target,destination)
    else:
        os.mkdir(destination)
        copyfile(target,destination)