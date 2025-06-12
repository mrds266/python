p1 = str(input("tem martelo? "))
p2 = str(input("ele voa? "))
p3 = str(input("tem cabelo loiro? "))
p4 = str(input("e um deus? "))
p5 = str(input("Mora na terra? "))

t = int(0)
c = int(0)

if(p1 == "sim"):
    t = t + 1
if(p2 == "sim"):
    t = t + 1
if(p3 == "sim"):
    t = t + 1
if(p4 == "sim"):
    t = t + 1
if(p5 == "sim"):
    t = t + 1



if(p1 == "não"):
    c = c + 1
if(p2 == "não"):
    c = c + 1
if(p3 == "não"):
    c = c + 1
if(p4 == "não"):
    c = c + 1
if(p5 == "não"):
    c = c + 1

print("thor " + str(t))
print("Capitão merica " + str(c))
