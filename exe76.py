cont = int(1)
numero = int(input("Qual tabuada você quer?  "))
for cont in range (1,10,1):
    total = numero * cont
    print(f"{numero} X {cont} = {total}")