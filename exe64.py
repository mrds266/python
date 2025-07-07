contador = int(0)
maior = int(0)
maiornome = str("")
menor = int(99999999999999)
menornome = str("")
while (contador < 5):
    contador = contador + 1

    nome = str(input("Fale seu nome "))
    sexo = str(input("fale seu sexo "))
    idade = int(input("Fale sua idade "))

    if( idade > maior and sexo == "h" ):
        maior = idade 
        maiornome  + nome
    if( idade < menor and sexo == "m" ):
        menor = idade
        menornome =  nome

print(f"Nome do homem mais velho é {maiornome} é nome da mulher masi jovem  {menornome}")
