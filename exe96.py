nu = [3,6,12,24,48,96,192,384,768,1536]

for k in nu:
    if(k == 3 or k ==6 or k == 96):
        print(f"${k}$")
    else:
        print(k)
print("----------------------------------")
numero = (3,0,0,0,0,0,0,0,0,0,0,0,0)

cont = int(0)
for cont in (10):
    numero[cont+1] = numero[cont]*2
    if(numero[cont] == 3 or numero[cont] == 6 or numero[cont] == 96):
        print(f"${numero[cont]}$")
    else:
        print(numero[cont])




















