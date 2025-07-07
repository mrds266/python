contador = int(0)
soma = int(0)

for contador in range(0,9,1):
    nu = int(input("Digite um numero logo "))

    
    soma = soma + nu

    if(nu == 999):
       
        break
    if(contador == 9):
       
        break

print(f"A soma dos numeros {soma} e numero de tentativas {contador}")














