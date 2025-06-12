salario1 = int(input("Digite seu salario  "))
salario2 = int(input("Digite seu salario  "))
salario3 = int(input("Digite seu salario  "))
salario4 = int(input("Digite seu salario  "))

maior = int(0)

if(salario1 > maior):
    maior = salario1
if(salario2 > maior):
    maior = salario2
if(salario3 > maior):
    maior = salario3
if(salario4 > maior):
    maior = salario4


print("O maior salario entre as pessoas ciradas é " + str(maior))

