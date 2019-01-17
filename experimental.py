import sqlite3
import os
from typing import Union

# def insertartist(number, artist):
#         conn = sqlite3.connect("artists.db;")
#         a = conn.cursor()
#         a.execute("CREATE TABLE artiststb (
#                 index integer,
#                 artist text);")
#         a.execute("INSERT INTO artisttb VALUES (:number, :artist);", {"number": number "artist": artist;})
#         conn.commit()

musicdirpath = "D:/" + str(os.environ.get("HOMEPATH")) + "\Musik"
print(str(os.environ.get("HOMEPATH")))
try:
    os.chdir(musicdirpath)
except FileNotFoundError:
    try:
        musicdirpath = "D:/" + str(os.environ.get("HOMEPATH")) + "\Music"
        os.chdir(musicdirpath)
    except FileNotFoundError:
        print("Problem with Music folder.")

for dirpath, dirnames, filenames in os.walk(musicdirpath):
    print("Pfad: ", dirpath)
    print("Ordner: ", dirnames)
    print("Datein: ", filenames)
    print()
