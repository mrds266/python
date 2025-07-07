idade = int(input("Digite sua idade "))
salario = int(input("Digite seu salario "))

print("sua idade é " + str(idade) + " anos e seu salario " + str(salario))

# format string

print( f"sua idade é {idade}  anos e seu salario  {salario}")

# estrututa de ripetição enquamto => while

contador = int()
#Portugol
#       enqunto (contador != 3){
#           contador = contador + 1
#           escreva("Digite seu salario")
#           leia(salario)
#           se(salario == 2000){
#               pare
#           }
#       }

while (contador != 3):
    contador = contador + 1 
    salario = int(input("Digite sua idade "))
    if(salario == 2000):
        break