import sqlite3

def databaseextender(artistname):
    artistsdatabaseobject = sqlite3.connect("artists.db")
    pointer = artistsdatabaseobject.cursor()
    # pointer.execute("create table artists_table (num, artist)")
    num = len(artistname)
    comp = [num, artistname]
    pointer.execute("select * from artists_table")
    artists = pointer.fetchall()
    print(artists)
    artistsdatabaseobject.commit()
    artistsdatabaseobject.close()