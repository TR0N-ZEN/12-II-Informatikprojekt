import sqlite3

liste = ["2Cellos", "ACDC", "ZZ Top"]
artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
# pointer.execute("create table artists_table (num, artist)")
for i in liste:
    num = liste.index(i)
    comp = [num, i]
    pointer.execute("insert into artists_table values (?, ?)", comp)
artistsdatabaseobject.commit()
artistsdatabaseobject.close()