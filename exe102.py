cont = int(0)
soma = int(0)
import random

a =[0,0,0,0]
nu = int(input("qual numero você esta procurando  "))
for cont  in range(4):
    a[cont] = random.randint(0,10)
    if(nu == a[cont]):
        soma = soma + nu



print(f"A soma é {soma}")
    
   








