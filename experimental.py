import sqlite3
import os


# def insertartist(number, artist):
#         conn = sqlite3.connect("artists.db;")
#         a = conn.cursor()
#         a.execute("CREATE TABLE artiststb (index integer, artist text);")
#         a.execute("INSERT INTO artisttb VALUES (?, ?)", (index, artist))
#         conn.commit()

# musicdirpath = "D:/" + str(os.environ.get("HOMEPATH")) + "\Musik"
# print(str(os.environ.get("HOMEPATH")))
# try:
#     os.chdir(musicdirpath)
# except FileNotFoundError:
#     try:
#         musicdirpath = "D:/" + str(os.environ.get("HOMEPATH")) + "\Music"
#         os.chdir(musicdirpath)
#     except FileNotFoundError:
#         print("Problem with Music folder.")

# for dirpath, dirnames, filenames in os.walk(musicdirpath):
#     print("Pfad: ", dirpath)
#     print("Ordner: ", dirnames)
#     print("Datein: ", filenames)
#     print()


homepath = str(os.environ.get("HOME"))
driveletters = ["A","B","C","D","E","F","G"]
for elements in driveletters:
    musicdirpath = elements + homepath[1:] + "\Musik"
    try:
        os.chdir(musicdirpath)
    except FileNotFoundError:
        pass
    else:
        print(musicdirpath)
        break
###########################################################################################################################################################################################
# which solution you think is better, not tested them so far (oh an I assume the user uses Windows as OS and maybe the system variable "HOME" doesn´t exist, so I may change it completely)
###########################################################################################################################################################################################
# while os.chdir(musicdirpath) = FileNotFoundError:
#     musicdirpath = driveletters[elements] + "/" + homepath + "\Musik"
#     elements = elements + 1
