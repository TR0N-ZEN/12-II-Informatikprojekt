import sqlite3

liste = ["2Cellos","ACDC","ZZ Top","Brother Dege","Volbeat","Linkin Park","Billy Talent","3 Doors Down","Franz Schubert","Bastille","Eisbrecher","Rammstein","InExtremo","Avicii","Mucc","Parov Stellar","Johnny Cash","Nickelback","George Ezra","The Dead South","Vicetone","Unlike Pluto","ABBA","The Animals","Beatles","BB King","David Guetta","Aerosmith","Saleri","Kaleo","Mumford and Sons","Sportfreunde Stiller","!panic at the disco","Saltatio mortis","Händel"]

artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
pointer.execute('''CREATE TABLE artists_table(num, artist)''')
artistsdatabaseobject.commit()
artistsdatabaseobject.close()

artistsdatabaseobject = sqlite3.connect("artists.db")
pointer = artistsdatabaseobject.cursor()
for i in liste:
    num = len(i)
    comp = [num, i]
    pointer.execute("INSERT INTO artists_table values (?, ?)", comp)
artistsdatabaseobject.commit()
artistsdatabaseobject.close()