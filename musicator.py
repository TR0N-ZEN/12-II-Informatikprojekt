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
                # if found == False:
                #         filenames_for_analyzation.append(f_name)

pieces = []
filenames_for_analyzation = []

global count
global count_row_1
global coun_row_2
count_row_2 = 0
count_row_1 = 0
count = 0

for e in os.scandir(musicdirpath): # filenames_for_analyzation:
        filenames_for_analyzation.append(e.name)
        z = e.name.split(" ") # returns a list of strings which in the the string e.name were "seperated" by space
        print(z)
        pieces.append(z)

for e in os.scandir(musicdirpath): # filenames_for_analyzation:
        f_name,f_ext = os.path.splitext(e.name)
        for r in pieces: # für elemente in Liste pieces
                if pieces.index(r) != filenames_for_analyzation.index(f_name): # wenn index von r in Liste pieces verschieden von index des Filenames ohne Dateiendung (f_name) in Liste filenames for analyzation
                        for t in r: # für elemente in Liste r
                                if f_name.find(t) != -1 and t != "-": # wenn t in f gefunden (nach IO von str.find() ist -1 nicht gefunden, d.h. wenn t nicht nicht in f gefunden)
                                        count = count + 1 # count für Häufigkeit des Funds von t in f
                                        i = r.index(t) # i ist index von t in r
                                        compound_guess_1 = t + " " + r[i+1] # Zusammenbasteln eines Strings aus gefundenem Teil t und ts Nachfolger in r (hier als r[i+1])
                                        if f_name.find(compound_guess_1) != -1:
                                                count_row_1 = count_row_1 + 1
                                                compound_guess_2 = compound_guess_1 + " " + r[i+2]
                                                if f_name.find(compound_guess_2) != -1:
                                                        count_row_2 = count_row_2 + 1
                                                        if count_row_2 > 4:
                                                                x = input("Is " + compound_guess_2 + " an artist? \n y/n: ")
                                                                if x == "y":
                                                                        print("Creating a folder an moving files")
                                                                else:
                                                                        print("okay") # NEXT UP  test on pieces in row combination
                                                elif count_row_1 > 4:
                                                        x = input("Is " + compound_guess_1 + " an artist? \n y/n: ")
                                                        if x == "y":
                                                                print("Creating a folder an moving files")
                                                        else:
                                                                print("okay") # NEXT UP  test on pieces in row combination
                                        else:
                                                if count > 4:
                                                        x = input("Is " + str(t) + " an artist? \n y/n: ")
                                                        if x == "y":
                                                                print("Creating a folder an moving files")
                                                        else:
                                                                print("okay") # NEXT UP  test on pieces in row combination