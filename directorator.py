import os
from shutil import copyfile
import pathlib

def directorator(musicdirpath,filename,path,interprete):
    target = pathlib.PurePath(path).joinpath(str(filename))
    destination = pathlib.PurePath(musicdirpath).joinpath(str(interprete))
    if os.path.isdir(destination) == True:
        copyfile(target,destination)
        # copy file with the passes name to this folder
    else:
        os.mkdir(interprete)
        copyfile(musicdirpath,destination)
        #copy files with the passed name into that folder