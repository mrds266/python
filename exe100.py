cont = int(0)
somapar =int(0)
impar = []
valor = [0,0,0,0]

for cont in range (4):

    valor[cont] =int(input("Digite um valor  "))
     
    if(valor[cont] %2==0):
       somapar = somapar + valor[cont]
    if(valor[cont] %2==1):
       impar.append(valor[cont])

print(f"A soma dos pares é {somapar}")
print(impar)







