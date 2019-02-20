import os
import subprocess
import sqlite3

# # extractor to extract mp3-file´s header
# try:
#     with open("The Dukes Of Hazzard ACDC - Shoot To Thrill.mp3", "rb") as mp3datbinary:
#         mp3dat = mp3headerbinary.decode("ascii")
#         mpe3header = mp3dat.read(147)
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
    for f in filenames:
        f_name, f_ext = os.path.splitext(f)
        if f_ext == ".mp3":
            print(f)
            for e in artists:
                if f_name.find(e[1]) != -1:
                    print(e[1])