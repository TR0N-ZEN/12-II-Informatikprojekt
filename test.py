import os
import sqlite3

# # extractor to extract mp3-file´s header
# try:
#     with open("The Dukes Of Hazzard ACDC - Shoot To Thrill.mp3", "rb") as mp3datbinary:
#         mp3dat = mp3headerbinary.decode("ascii")
#         mpe3header = mp3dat.read(147)
# except FileNotFoundError:
#     mp3header = None
# print(mp3header)
print(os.getcwd)
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabaseobject.close()
print(artists)