import os

def pathfinder():
    homepath = str(os.environ.get("HOME"))
    print(homepath[1:])
    driveletters = ["A", "B", "C", "D", "E", "F", "G"]
    for elements in driveletters:
        musicdirpath = driveletters[elements] + homepath[1:] + "\Musik"
        try:
            os.chdir(musicdirpath)
            return(musicdirpath)
            break
        except FileNotFoundError:
            pass
            