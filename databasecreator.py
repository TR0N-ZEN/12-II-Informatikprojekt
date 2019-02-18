import sqlite3
artist = ["Maxim Schunk", "Linkin Park"]
artistsdatabaseobject =sqlite3.connect(artists.db)
pointer = artistsdatabaseobject.cursor()
pointer.execute("create table artists_table (artist)")
pointer.executemany("insert into artists_table values (?)", artist)
pointer.commit()
pointer.close()