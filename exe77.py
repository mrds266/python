contador = int(0)
par = int(0)
impar = int(0)
somaimpar = int(0)
somapar = int(0)


for contador in range(0,4,1):

    n = int(input("Digite um numero "))
    soma = int(n + n)
    if(n %2==0):
        par = par + 1
        somapar = somapar + n
    if(n %2==1):
        impar =impar + 1
        somaimpar = somaimpar + n

print(f"Foram cadastrados {par} números pares")
print
print(f"Foram cadastrados {impar} números impares")
print
print(f"A soma dos pares é {somapar}")
print
print(f"A soma dos impares é {somaimpar}")
print
print(f"A soma geral é {soma}")
