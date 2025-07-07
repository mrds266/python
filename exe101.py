cont = int(0)
somaimpar =int(0)
par = []
valor = [0,0,0,0]

for cont in range (4):

    valor[cont] =int(input("Digite um valor  "))
     
    if(valor[cont] %2==1):
       somaimpar = somaimpar + valor[cont]
    if(valor[cont] %2==0):
       par.append(valor[cont])

print(f"A soma dos pares é {somaimpar}")
print(par)







