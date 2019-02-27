import os

def pathfinder(language):
    homepath = str(os.environ.get("HOME"))
    langdict = {
        "de": "\\Musik",
        "en": "\\Music"
    }
    driveletters = ["A", "B", "C", "D", "E", "F", "G"]
    for i in driveletters:
        musicdirpath = i + homepath[1:] + langdict[language]
        if os.path.isdir(musicdirpath) == True:
            return musicdirpath
        else:
            pass