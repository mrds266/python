

a0_25 = int(0)
a26_50 = int(0)
a51_75 = int(0)
a76_100 = int(0)
contador = int(0)

while(contador < 5):
    contador = contador + 1
    nu = int(input("Digite um numero "))

    if(nu > 0 and nu < 25 ):
        a0_25 = a0_25 + 1
    if(nu > 26 and nu < 50 ):
        a26_50 = a26_50 + 1
    if(nu > 51 and nu < 75 ):
        a51_75 = a51_75 + 1
    if(nu > 76 and nu < 100 ):
        a76_100 = a76_100 + 1

print(f"No final mostre quantos números estão entre [0-25]   {a0_25}   ")
print(f"No final mostre quantos números estão entre [26-50]  {a26_50}  ")
print(f"No final mostre quantos números estão entre [51-75]  {a51_75}  ")
print(f"No final mostre quantos números estão entre [76-100] {a76_100} ")