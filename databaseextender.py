import sqlite3
import datetime

def databaseextender(artistname):
    artistsdatabaseobject = sqlite3.connect("artists.db")
    pointer = artistsdatabaseobject.cursor()
    # for creating a table
    # pointer.execute("create table artists_table (num, artist)")
    length = len(artistname)
    d = datetime.date.today()
    # change num to date, because i dont see the effectiveness of implementing len yet and with date you can reset your database
    # add number of artist matches in files, so that it can be assumed with higher porbability to be an artist in other files
    comp = [length, artistname, d]
    pointer.execute("INSERT INTO artists_table values (?, ?, ?)", comp)
    artistsdatabaseobject.commit()
    artistsdatabaseobject.close()