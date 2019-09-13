import os

def pathfinder():
    x = str(os.environ.get("TEMP"))
    print(x)
    if x.find("User") != -1:
        lang = "\\Music"
    if x.find("Benutzer") != -1:
        lang = "\\Musik"
    y = x.split("\\")
    middle = ":\\" + str(y[1]) + "\\" + str(y[2])
    driveletters = ["A", "B", "C", "D", "E", "F", "G"]
    for e in driveletters:
        musicdirpath = e + middle + lang
        if os.path.isdir(musicdirpath) == True:
            return musicdirpath