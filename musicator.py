import os
# from typing import Union
import sqlite3
from pathfinder import pathfinder
from extractor import extractor
# from scanner import scanner
# from databaseextender import databaseextender
# from renamer import renamer
# from directorator import directorator


language = input("Enter de for German or en for English: ")
musicdirpath = pathfinder(language)
print("Dein  Musikordner befindet sich in: " + str(musicdirpath))
print("-------------------------------------------------------------------------")

pathfiledict = {}
class filesindict:
        def _init_(self, path, musicfilesinpath):
                

for dirpath, dirnames, musicfiles in os.walk(musicdirpath):
        # print("Pfad: ", dirpath)
        # print("Ordner: ", dirnames)
        # print("Datein: ", filenames)
        pathfiledict[dirpath] = musicfiles
        # for files in filenames:
        #         mp3header = extractor(files)
        #         metadata = scanner(mp3header)
        #         databaseextender(metadata)
        #         renamer(metadata)
        #         directorator(metadata)

for i in pathfiledict:
        print(i)
        print(pathfiledict[i])
        print()
        print(extractor(pathfiledict))
        