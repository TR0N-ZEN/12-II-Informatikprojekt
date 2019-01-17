import os


def extractor(filename):
    try:
        with open(filename, "rb") as mp3dat:
            mp3header = mp3dat.read(147)
    except FileNotFoundError:
        mp3header = None
    return mp3header
