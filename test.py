import os
import pathlib

os.chdir(pathlib.PurePath("C:\\Users\\Emil\\Music"))
for e in os.scandir():
    i = str(e)
    if i.find("Panic! At The Disco") != -1:
        print("found")