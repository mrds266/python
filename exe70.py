contador = int(0)

while (contador < 99999999):
    nu = int(input("Digite um numero "))
    
    if( nu == 999):
        soma = int(nu + nu)
        print(f"tentativa {contador}")
        print(f"A soma {soma}")
        break