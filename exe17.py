valor1 = int(input("Digite um valor "))
valor2 = int(input("Digite um valor "))
valor3 = int(input("Digite um valor "))

contador = int(0)

if(valor1 > 25):
    contador = contador + 1

if(valor2 > 25):
    contador = contador + 1
if(valor3 > 25):
    contador = contador + 1

print("Encontramos " + str(contador) + " numero maior do que 25")