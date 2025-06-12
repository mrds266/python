nome = str(input("fale seu nome "))
nota1 = int(input("fale sua nota "))
nota2 = int(input("fale sua nota "))
nota3 = int(input("fale sua nota "))
nota4 = int(input("fale sua nota "))

media = int( nota1 + nota2 + nota3 + nota4 / 4)

if(media >= 7 ):
    print(nome +" aprovado")
else:
    print(nome +" reprovado")
