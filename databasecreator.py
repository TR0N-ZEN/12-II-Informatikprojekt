import sqlite3

artistsdatabaseobject =sqlite3.connect(
    host="localhsot"
    user="scanner"
    passwd="1123"
    database="artists"
    )
pointer = artistsdatabaseobject.cursor()
pointer.execute("CREATE TABLE artists_table (artist)")
pointer.commit()
pointer.close()