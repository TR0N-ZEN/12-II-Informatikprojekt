import os

def extractor(filename):
    try:
        with open(filename, "rb") as mp3dat:
            mp3header = mp3dat.read(147)
    except FileNotFoundError:
        mp3header = None
    return mp3header
v = str(extractor("Maxim Schunk - Give It All (Official Music Video).mp3"))
print(v[2:147])

text = str(ID3\x04\x00\x00\x00\x00ZrTIT2\x00\x00\x003\x00\x00\x03)
for i in text
