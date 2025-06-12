valor1 = int (input("Dgite o 1º valor  "))
valor2 = int (input("Dgite o 2º valor  "))
valor3 = int (input("Dgite o 3º valor  "))
contadorpar = int(0)
contadorimpar = int(0)

if(valor1 %2==0 ):
    contadorpar = contadorpar + 1
if(valor2 %2==0 ):
    contadorpar = contadorpar + 1
if(valor3 %2==0 ):
    contadorpar = contadorpar + 1

if(valor1 %2==1 ):
    contadorimpar = contadorimpar + 1
if(valor2 %2==1 ):
    contadorimpar = contadorimpar + 1
if(valor3 %2==1 ):
    contadorimpar = contadorimpar + 1

print("Foram encontrados numeros "+ str(contadorpar) +" pares e numeros " + str(contadorimpar) + "impares")
 
    