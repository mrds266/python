numero1 = int(input("Digite um numero "))
numero2 = int(input("Digite um numero "))
numero3 = int(input("Digite um numero "))
numero4 = int(input("Digite um numero "))

contadorpar = int(0)
somapar = int(0)
maiorpar = int(0)

if(numero1 %2==0):
    somapar = somapar + numero1
if(numero2 %2==0):
    somapar = somapar + numero2
if(numero3 %2==0):
    somapar = somapar + numero3
if(numero4 %2==0):
    somapar = somapar + numero4

if(numero1 %2==0):
    contadorpar = contadorpar + 1
    
if(numero2 %2==0):
    contadorpar = contadorpar + 1
    
if(numero3 %2==0):
    contadorpar = contadorpar + 1
if(numero4 %2==0):
    contadorpar = contadorpar + 1

if(numero1 %2==0 and numero1 > maiorpar ):
        maiorpar = numero1        
if(numero2 %2==0 and numero2 > maiorpar):
        maiorpar = numero2   
if(numero3 %2==0 and numero3 > maiorpar):
        maiorpar = numero3
if(numero4 %2==0 and numero4 > maiorpar):
        maiorpar = numero4
   
   
print("Foram Digitados " + str(contadorpar) + "números pares")
print("A soma desses números pares é " + str(somapar))
print("O maior numero par é " + str(maiorpar))