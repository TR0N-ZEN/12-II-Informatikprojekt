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
###########################################################################################################################################################################################
# which solution you think is better, not tested them so far (oh an I assume the user uses Windows as OS and maybe the system variable "HOME" doesn´t exist, so I may change it completely)
###########################################################################################################################################################################################
    while os.chdir(musicdirpath) = FileNotFoundError:
        musicdirpath = driveletters[elements] + "/" + str(os.environ.get("HOMEPATH")) + "\Musik"
        elements = elements + 1
