a = "Avicii - Addicted to you"
b = "Avicii - Hey Brother"
c = "Avicii - For a better day"
filenames = [a, b, c]
pieces = []
def top(filenames):
    for e in filenames:
        z = e.split(" ")
        pieces.append(z)

count = 0
def one_under_top(filenames, pieces):
    for e in filenames:
        for r in pieces:
            if pieces.index(r) != filenames.index(e):
                for t in r:
                    if e.find(t) != -1:
                        if t != "-":
                            print(t)

top(filenames)
one_under_top(filenames, pieces)

if count > 5:
    print("Found Artist" + str() + " with high probability")