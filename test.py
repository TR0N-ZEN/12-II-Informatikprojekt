import os
import subprocess
import sqlite3

# try:
#     with open("The Dukes Of Hazzard ACDC - Shoot To Thrill.mp3", "rb") as mp3dat:
#         mp3header = mp3dat.read(147)
# except FileNotFoundError:
#     mp3header = None
# print(mp3header)

artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()
# print(artists)

# print(os.getcwd())
# output = subprocess.check_output("dir /d", shell=True)
# text = output.decode("ascii")
# lines = text.splitlines()
# for i in lines:
#     if i.find(".mp3") != -1:
#         print(i)
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for e in filenames:
        if e.find(".mp3") != -1:
            print(e)
            for i in artists:
                if e.find(i[1]) != -1:
                    print(i[1])