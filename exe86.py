contador = int(0)

while (contador < 999999):

    import random

    s = random.randint(1,10)

    chute = str(input("chute um numero "))

    if(chute > s):
        print("Você errou tente um numero menor")
    if(chute < s):
        print("Você errou tente um numero maior")
    if(chute == s):
        print(f"Sucesso você acertou após {contador} tentativas")
        break

