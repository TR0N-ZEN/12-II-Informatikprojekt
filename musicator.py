import os
import sqlite3
from pathfinder import pathfinder
# from extractor import extractor
# from filenameanalyzer import filenameanalyzer
# from renamer import renamer
from directorator import directorator
from databaseextender import databaseextender

musicdirpath = pathfinder() # MODULE
# print("-------------------------------------------------------------------------")
# print("Your music is located in: " + musicdirpath)
# print("-------------------------------------------------------------------------")

# get elements from database (e[0]=artistname.len(); e[1]=artistname)
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()

def check_with_database():
        # filenames = os.scandir(musicdirpath) # optional for only scanning without scanning subfolders in comparison to os.walk()
        for dirpath, dirnames, filenames in os.walk(musicdirpath):
                for f in filenames:
                        f_name,f_ext = os.path.splitext(f)
                        for e in artists:
                                if f_name.find(e[1]) != -1:
                                        directorator(musicdirpath,str(f),str(dirpath),e[1]) # MODULE

filenames_for_analyzation= []
pieces = []
def get_remaining():
        # filenames for string comparison if no artist has been found in the database
        for e in os.scandir(musicdirpath):
                filenames_for_analyzation.append(e.name)
                z = e.name.split(" ") # returns a list of strings which in the the string e.name were "seperated" by space
                pieces.append(z)
        print(z)

global count
count = 0
global not_necessary_to_query
not_necessary_to_query = []
def analyzer(f,r,compound_guess,nextpart,count,legacy):
        if f.find(compound_guess) != -1 and compound_guess not in not_necessary_to_query:
                print(compound_guess + "|")
                legacy = compound_guess # savin the confirmed / approved compound_guess for next recursion so that if it fails it will go to else and return legacy, the last ompound_guess that worked
                i = r.index(nextpart) # getting index of nextpart
                nextpart = r[i+1] # redefining nextpart as the item following the current nextpart in list r
                compound_guess = compound_guess + " " + nextpart
                analyzer(f,r,compound_guess,nextpart,count + 1,legacy)
        elif count > 3:
                q = input("Is " + legacy + " an artist?\ny/n: ")
                if q == "y":
                        print("Nice we´ll be creating a folder for you" + legacy)
                        # add artist to database inorder to run comparison with database again and copy all those whose artist was just added
                        databaseextender(legacy) # MODULE
                        # directorator(musicdirpath,f,musicdirpath,legacy) - bad idea, as it causes only the third and following files to be copied
                        not_necessary_to_query.append(legacy)
                elif q == "n":
                        not_necessary_to_query.append(legacy) # strigs which were assumed as artisnames but werent, because user said they arent

def start_analyzer(filenames, pieces):
        for f in filenames:
                for r in pieces:
                        if pieces.index(r) != filenames.index(f) and f.find(r[0]) != -1: # r of pieces and f of filenames with the same index suggests that r is a derivative of f which causes a 100% match causing problems in the matching mechanism 
                                analyzer(f,r,r[0],r[0],0,"") # passed variables: f = filename; r = list of filenamesubstrings which are followed by a space; r[0]; r[1]; count = 0; legacy is an empty string as there is no legacy value

check_with_database()
start_analyzer(filenames_for_analyzation,pieces)
# print(not_necessary_to_query)
check_with_database()