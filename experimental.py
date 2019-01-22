import os

for dirpath, dirnames, filenames in os.walk(top):
        print("Pfad: ", dirpath)
        print("Ordner: ", dirnames)
        print("Datein: ", filenames)
        print()
