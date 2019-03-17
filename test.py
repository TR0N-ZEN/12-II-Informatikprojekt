import sqlite3

a = "Avicii and Friends Addicted to you"
b = "Avicii and Friends Hey Brother"
c = "Avicii and Friends For a better day"
d = "Avicii and Friends Random"
filenames = [a, b, c, d]
pieces = []

def top(filenames):
    for e in filenames:
        z = e.split(" ")
        pieces.append(z)

global count
count = 0

