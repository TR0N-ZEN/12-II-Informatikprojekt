import sqlite3

artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute("create table artists_table (artist)")
# pointer.execute("insert into artists_table values (?)", liste)
artistsdatabaseobject.commit()
artistsdatabaseobject.close()