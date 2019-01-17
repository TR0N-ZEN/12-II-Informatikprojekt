import os
import mysql.connector

def scanner(mp3header):
    # enter the following in the console to install mysql connector: python -m pip install mysql-connector
    # inetgrate database an loop through; learn parsing / checking if a string is part of another string, the compare string which is checked if it is in the other comes out of a list, so its an elemnt of the list an the lements can be looped throug
    databaseinterpretes = mysql.connector.connect(
        host="localhsot"
        user="scanner"
        passwd="1123"
        database="dbinterpretes" # moment raff ich grad nicht
    )
    print(databaseinterpretes) # for checking
    for i in # amount of artist entries in database
    databaseartist = ("Maxim Schunk", "Linkin Park")
    if mp3header.find(databaseartist[i]):
        class metadata:
            def __init__(self, interprete, title):
                    self.interprete = databaseartist
                    self.title = title
    else:
        i = i + 1
    return(metadata) # return objects possible otherwise take tuple?
    
