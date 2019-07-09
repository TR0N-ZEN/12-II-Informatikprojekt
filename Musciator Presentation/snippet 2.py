import math

a = input("Name eingeben: ")
b = input("Anzahl eingeben: ")

def function(a):
    c = c + a
    count = count + 1
    print(a)
    while count < b:
        function(c)
    print(count)

print(function(a))