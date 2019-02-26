import os
import sqlite3

def scanner(mp3header):
#     class metadata:
#         def __init__(self, interprete, title):
#             self.interprete = databaseartist
#             self.title = title
    artistsdatabaseobject = sqlite3.connect("artists.db")
    pointer = artistsdatabaseobject.cursor()
    pointer.execute("select * from artists_table")
    artists = pointer.fetchall()
    print(artists)
    for i in artists:
        if mp3header.find(i[1]):
                return i[1]
        else:
                pass