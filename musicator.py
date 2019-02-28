import os
import sqlite3
from pathfinder import pathfinder
# from extractor import extractor
# from scanner import scanner
# from filenameanalyzer import filenameanalyzer
# from databaseextender import databaseextender
# from renamer import renamer
from directorator import directorator

language = input("Enter de for German or en for English: ")
musicdirpath = pathfinder(language)
print("-------------------------------------------------------------------------")
print("Dein Musikordner befindet sich in: " + str(musicdirpath))
print("-------------------------------------------------------------------------")

#get elements from database (e[0]=artistname.len(); e[1]=artistname)
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()

#filenames for string comparison if no artist has been found in the database
filenames_for_analyzation= []

global artistname_from_filename
artistname_from_filename = "NONE"
global found
found = False

#filenames = os.scandir(musicdirpath) # optional for only scanning without scanning subfolders in comparison to os.walk()
for dirpath, dirnames, filenames in os.walk(musicdirpath):
    for f in filenames:
        f_name,f_ext = os.path.splitext(f)
        if f_ext == ".mp3":
                found = False
                for e in artists:
                        if f_name.find(e[1]) != -1:
                                directorator(musicdirpath,f,dirpath,e[1])
                                found = True
                        else:
                                pass
                if found == False:
                        filenames_for_analyzation.append(f_name)
print(filenames_for_analyzation)