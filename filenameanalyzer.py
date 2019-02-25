import os

def filenameanalyzer:
    artistsdatabaseobject =sqlite3.connect("artists.db")
    pointer = artistsdatabaseobject.cursor()
    pointer.execute("select * from artists_table")
    artists = pointer.fetchall()
    for e in artists:
        if f_name.find(e[1]) != -1:
            return e[1]