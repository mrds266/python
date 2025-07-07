par = int(0)
somapar = int(0)
contador = int(0)

for contador in range (0,6,1):

    nu = int(input("Digite um numero "))

    if(nu %2==0):
        par = par + 1
        somapar = somapar + nu

print(f"quantidade de numeros pares e {par} e a soma {somapar}")







