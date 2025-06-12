a = int(input("Dgite um numero "))
b = int(input("Dgite um numero "))
c = int(input("Dgite um numero "))

maior = int(0)
menor = int(0)
meio = int(0)
if(a> b and a > c and b > c):
    maior = a 
    meio = b 
    menor =c
if(a > b and a > c and c > b ):
    maior = a 
    meio = c
    menor = b
if(b > a and b > c and a > c):
    maior =  b
    meio = a
    menor = c
if( b > a and b > c and c > a):
    maior =  b
    meio = c
    menor = a

if(c > a and c > b and  a > b):
    maior =  c
    meio = a
    menor = b
if(c > a and c > b and b > a):
    maior =  c
    meio = b
    menor = a
else:
    print("os números são iguais por isso não existe maior ou menor")


print("o maior é "+ maior +" o do meio é "+ meio +" e o menor é " + menor)