def maior(nu):
    maior = int(0)
    if(nu > maior):
        maior = nu
    return maior

def menor(nu):
    menor = int(0)
    if(nu < menor):
        menor = nu
    return menor

def media(maior,menor):
    media = int(0)
    soma = int(maior + menor)
    media = soma / 2
    print(f"A media e {media}")
