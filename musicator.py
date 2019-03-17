import os
import sqlite3
from pathfinder import pathfinder
# from extractor import extractor
# from filenameanalyzer import filenameanalyzer
# from renamer import renamer
from directorator import directorator
from databaseextender import databaseextender

language = input("Enter de for German or en for English: ")
musicdirpath = pathfinder(language) # MODULE
print("-------------------------------------------------------------------------")
print("Dein Musikordner befindet sich in: " + musicdirpath)
print("-------------------------------------------------------------------------")

# get elements from database (e[0]=artistname.len(); e[1]=artistname)
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()

# filenames for string comparison if no artist has been found in the database
filenames_for_analyzation= []

# filenames = os.scandir(musicdirpath) # optional for only scanning without scanning subfolders in comparison to os.walk()
for dirpath, dirnames, filenames in os.walk(musicdirpath):
    for f in filenames:
        f_name,f_ext = os.path.splitext(f)
        for e in artists:
                if f_name.find(e[1]) != -1:
                        directorator(musicdirpath,f,dirpath,e[1]) # MODULE
                else:
                        filenames_for_analyzation.append(f_name) # names of files which had no match with artist entries in database

pieces = []

for e in filenames_for_analyzation:
        z = f_name.split(" ") # pieces is an array / 2D list, 1st dimension elements are lists which contain (2nd dimension) strings which originate from the the entries in filenames_for_analyzation
        pieces.append(z)

# for e in os.scandir(musicdirpath):
#         filenames_for_analyzation.append(e.name)
#         z = e.name.split(" ") # returns a list of strings which in the the string e.name were "seperated" by space
#         print(z)
#         pieces.append(z)

global count
count = 0
global final
final = []
global not_necessary_to_query
not_necessary_to_query = []

def analyzer(f,r,compound_guess,nextpart,count,legacy):
        if compound_guess not in not_necessary_to_query and f.find(compound_guess) != -1 and count < len(r):
                count = count + 1
                i = r.index(nextpart) # getting index of nextpart
                nextpart = r[i+1] # redefining nextpart as the item following the current nextpart in list r
                legacy = compound_guess # savin the confirmed / approved compound_guess for next recursion so that if it fails it will go to else and return legacy, the last ompound_guess that worked
                compound_guess = compound_guess + " " + nextpart
                analyzer(f,r,compound_guess,nextpart,count,legacy)
        elif count == 3:
                q = input("Is " + legacy + " an artist?\n y/n")
                if q == "y":
                        print("Nice we´ll be creating a folder for you")
                        # add artist to database inorder to run comparison with database again and copy all those whose artist was just added
                        databaseextender(legacy) # MODULE
                        # directorator(musicdirpath,f,musicdirpath,legacy) - bad idea, as it causes only the third and following files to be copied
                elif q == "n":
                        not_necessary_to_query.append(legacy)

global x
x = 0

def start_analyzer(filenames, pieces):
        for f in filenames:
                for r in pieces:
                        if pieces.index(r) != filenames.index(f) and f.find(r[0]) != -1: # r of pieces and f of filenames with the same index suggests that r is a derivative of f which causes a 100% match causing problems in the matching mechanism 
                                analyzer(f,r,r[0],r[0],0,"") # passed variables: f = filename; r = list of filenamesubstrings which are followed by a space; r[0]; r[1]; count = 0; legacy is an empty string as there is no legacy value
        print(final)

start_analyzer(filenames_for_analyzation,pieces)