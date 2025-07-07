def investigar(a,b,c,d,e):
    ponto = int(0)
    if(a == "sim"):
        ponto = ponto +1
    if(b == "sim"):
        ponto = ponto +1
    if(c == "sim"):
        ponto = ponto +1
    if(d == "sim"):
        ponto = ponto +1
    if(c == "sim"):
        ponto = ponto +1
    
    if(ponto == 2):
        print("Suspeita")
    if(ponto == 3 or ponto == 4):
        print("Cúmplice")
    if(ponto == 5):
        print("Assassino")
    
    