import math

a = input("Laenge erste Kathete eingeben")
b = input("Laenge erste Kathete eingeben")

def triangle(a, b):
    c = math.sqrt(a*a + b*b)
    return c

print(triangle(a,b))