contador = int(0)

while (contador < 999):
    usuario = str(input("Fale seu usuario "))
    nu = int(input("Digite um numero"))

    r = str(input("Quer par ou impar? "))
    import random

    s = random.randint(1,9)

    soma = int(nu + s)

    if(soma %2==0 and nu %2==0):
        print("ganhou")
        print(f"Tentativas  {contador}")
        break
    if(soma %2==1 and nu %2==1):
        print("ganhou")
        print(f"Tentativas  {contador}")
        break
    else:
        print("derrotado pelo carlão")  

