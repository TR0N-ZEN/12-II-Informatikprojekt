x = "hello mate"
y = "hello there"
a = 0
o = 1
while a < len(x): 
    while o <= len(x):
        print(y.find(x[a:o]))
        o = o + 1 
    a = a + 1 
    o = 0