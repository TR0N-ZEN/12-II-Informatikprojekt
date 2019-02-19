import sqlite3

artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("select * from artists_table")
artists = pointer.fetchall()
artistsdatabasIdeobject.close()
print(artists)