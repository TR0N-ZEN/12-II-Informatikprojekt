import os

def pathfinder():
    driveletters = ["A:", "B:", "C:", "D:", "E:", "F:", "G:"]
    for elements in driveletters:
        musicdirpath = driveletters[elements] + "/" + str(os.environ.get("HOMEPATH")) + "\Musik"
        try:
            os.chdir(musicdirpath)
            return(musicdirpath)
            break
        except FileNotFoundError:
            try:
                musicdirpath = driveletters[elements] + "/" + str(os.environ.get("HOMEPATH")) + "\Music"
                os.chdir(musicdirpath)
                return(musicdirpath)
                break
            except FileNotFoundError:
