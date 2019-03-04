# a = "Avicii - Addicted to you"
# b = "Avicii - Hey Brother"
# c = "Avicii - For a better day"
# filenames = [a, b, c]
# pieces = []
# def top(filenames):
#     for e in filenames:
#         z = e.split(" ")
#         pieces.append(z)

# count = 0
# def one_under_top(filenames, pieces):
#     for e in filenames:
#         for r in pieces:
#             if pieces.index(r) != filenames.index(e):
#                 for t in r:
#                     if e.find(t) != -1:
#                         if t != "-":
#                             global count
#                             count = count + 1
#                             if count > 5:
#                                 x = input("Is " + str(t) + " an artist? \n y/n: ")
#                                 if x == "y":
#                                     print("Creating a fodler an moving files")
#                                 else:
#                                     print("okay")
# top(filenames)
# one_under_top(filenames, pieces)
import os
x = []
homepath = str(os.environ.get("HOME")) + "\\Music"
x = os.scandir(homepath)
for e in os.scandir(homepath):
    print(e.name)