import os

def pathfinder():
    homepath = str(os.environ.get("HOME"))
    driveletters = ["A", "B", "C", "D", "E", "F", "G"]
    for i in driveletters:
        musicdirpath = i + homepath[1:] + "\Musik"
        print(msucidirpath)
        try:
            os.chdir(musicdirpath)
        except FileNotFoundError:
            pass
        else:
            return(musicdirpath)
            break
