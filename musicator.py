import os
# from typing import Union
# import sqlite3
from pathfinder import pathfinder
# here is the os.walk
# from extractor import extractor
# from scanner import scanner
# from databaseextender import databaseextender
# from renamer import renamer
# from directorator import directorator

print("Enter")
print("de for German") 
print("en for English")
language = str(input())
musicdirpath = pathfinder(language)
print(musicdirpath)

# for dirpath, dirnames, filenames in os.walk(musicdirpath):
#         print("Pfad: ", dirpath)
#         print("Ordner: ", dirnames)
#         print("Datein: ", filenames)
#         print()

# mp3header = extractor(chosen_file)
# # print(mp3header)

# metadata = scanner(mp3header)  # may be problems with var as it gets a tuple as value send back by parser()
# print(str(metadata[0]) + str(metadata[1]))  # checking
# databaseextender(metadat[0])
# renamer(metadata[0], metadata[1])#looks frankenstine
# yet not thought about much
# directorator()
