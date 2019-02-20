import os
import sqlite3

def scanner(mp3header):
#     class metadata:
#         def __init__(self, interprete, title):
#             self.interprete = databaseartist
#             self.title = title
    artistsdatabaseobject =sqlite3.connect("artists.db")
    pointer = artistsdatabaseobject.cursor()
    pointer.execute("select * from artists_table")
    artists = pointer.fetchall()
    for e in artists:
        if mp3header.find(e):
                return e
                break
        else:
                pass