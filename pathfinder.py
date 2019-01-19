import os

def pathfinder():
    homepath = str(os.environ.get("HOME"))
    driveletters = ["A","B","C","D","E","F","G"]
    for elements in driveletters:
        musicdirpath = elements + homepath[1:] + "\Musik"
        try:
            os.chdir(musicdirpath)
        except FileNotFoundError:
            pass
        else:
            return(musicdirpath)
            break
