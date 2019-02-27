import os
import sqlite3
from pathfinder import pathfinder
# from extractor import extractor
# from scanner import scanner
# from filenameanalyzer import filenameanalyzer
# from databaseextender import databaseextender
# from renamer import renamer
# from directorator import directorator

language = input("Enter de for German or en for English: ")
musicdirpath = pathfinder(language)
print("Dein Musikordner befindet sich in: " + str(musicdirpath))
print("-------------------------------------------------------------------------")
print(os.getcwd())
print("-------------------------------------------------------------------------")
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()
global artistname_from_filename
artistname_from_filename = "NONE"
for dirpath, dirnames, filenames in os.walk(musicdirpath):
    for f in filenames:
        f_name, f_ext = os.path.splitext(f)
        if f_ext == ".mp3":
                #mp3header = extractor(f)
                #metadata = scanner(mp3header) # artistsname
                for e in artists:
                        if f_name.find(e[1]) != -1:
                                artistname_from_filename = e[1]
                print(artistname_from_filename)
                # databaseextender()
                # renamer(metadata)
                # directorator(musicdirpath,f,dirpath,artist_from_filename)