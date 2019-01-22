import sqlite3
import os

# def insertartist(number, artist):
#         conn = sqlite3.connect("artists.db;")
#         a = conn.cursor()
#         a.execute("CREATE TABLE artiststb (index integer, artist text);")
#         a.execute("INSERT INTO artisttb VALUES (?, ?)", (index, artist))
#         conn.commit()
#
# for dirpath, dirnames, filenames in os.walk(musicdirpath):
#     print("Pfad: ", dirpath)
#     print("Ordner: ", dirnames)
#     print("Datein: ", filenames)
#     print()
homepath = str(os.environ.get("HOME"))
driveletters = "ABCDEFG"
print(len(driveletters))
for x in driveletters:
    musicdirpath = driveletters[x] + homepath[1:] + "\Musik"
    try:
        os.chdir(musicdirpath)
        print(musicdirpath)
        break
    except FileNotFoundError:
        pass


###########################################################################################################################################################################################
# which solution you think is better, not tested them so far (oh an I assume the user uses Windows as OS and maybe the system variable "HOME" doesn´t exist, so I may change it completely)
###########################################################################################################################################################################################
# os.chdir(musicdirpath)
# while os.chdir(musicdirpath) = FileNotFoundError:
#     musicdirpath = driveletters[elements] + homepath[1:] + "\Musik"
#     elements = elements + 1