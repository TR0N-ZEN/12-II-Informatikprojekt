import os

def pathfinder():
    driveletters = ["A:", "B:", "C:", "D:", "E:", "F:", "G:"]
    for elements in driveletters:
        musicdirpath = driveletters[elements] + "/" + str(os.environ.get("HOMEPATH")) + "\Musik"
        try:
            os.chdir(musicdirpath)
        except FileNotFoundError:
            try:
                musicdirpath = driveletters[elements] + "/" + str(os.environ.get("HOMEPATH")) + "\Music"
                os.chdir(musicdirpath)
            except FileNotFoundError:
                print("Problem with Music folder.")

    for dirpath, dirnames, filenames in os.walk(musicdirpath):
        print("Pfad: ", dirpath)
        print("Ordner: ", dirnames)
        print("Datein: ", filenames)
        print()
