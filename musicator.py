import os
# from typing import Union
import sqlite3
from pathfinder import pathfinder
from extractor import extractor
from scanner import scanner
from filenameanalyzer import filenameanalyzer
# from databaseextender import databaseextender
# from renamer import renamer
from directorator import directorator

language = input("Enter de for German or en for English: ")
musicdirpath = pathfinder(language)
print("Dein Musikordner befindet sich in: " + str(musicdirpath))
print("-------------------------------------------------------------------------")

for dirpath, dirnames, filenames in os.walk(musicdirpath):
    for f in filenames:
        f_name, f_ext = os.path.splitext(f)
        if f_ext == ".mp3":
                mp3header = extractor(files)
                metadata = scanner(mp3header) # artistsname
                artist_from_filename = filenameananalyzer(f_name)
                # databaseextender()
                # renamer(metadata)
                directorator(artist_from_filename)