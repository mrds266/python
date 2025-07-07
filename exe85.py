contador = int(0)
valor  = int(input("Qaul o valor da venda "))
n50 = int(0)
n20 = int(0)
n10 = int(0)
n2 = int(0)
n1 = int(0)

while (valor > 0 ):

    if(valor >= 50):
        n50 = n50 + 1
        valor = valor - 50
    elif(valor >= 20):
        n20 = n20 + 1    
        valor = valor - 20

    elif(valor >= 10):
        n10 = n10 + 1    
        valor = valor - 10

    elif(valor >= 2):
        n2 = n2 + 1    
        valor = valor - 2
    
    elif(valor >= 1):
        n1 = n1 + 1    
        valor = valor - 1

print(f"Quantidade de notas de 50 {n50}")
print(f"Quantidade de notas de 20 {n20}")
print(f"Quantidade de notas de 10 {n10}")
print(f"Quantidade de notas de 2 {n2}")
print(f"Quantidade de notas de 1 {n1}")