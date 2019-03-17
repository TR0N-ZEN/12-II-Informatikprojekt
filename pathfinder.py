import os

def pathfinder(language):
    x = str(os.environ.get("TEMP"))
    y = x.split("\\")
    middle = ":\\" + str(y[1]) + "\\" + str(y[2])
    langdict = {
        "de": "\\Musik",
        "en": "\\Music"
    }
    driveletters = ["A", "B", "C", "D", "E", "F", "G"]
    for i in driveletters:
        musicdirpath = i + middle + langdict[language]
        if os.path.isdir(musicdirpath) == True:
            return musicdirpath