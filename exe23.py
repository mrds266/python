compra1 = int (input("Dgite o 1º valor  "))
compra2 = int (input("Dgite o 2º valor  "))
compra3 = int (input("Dgite o 3º valor  "))
soma = int(compra1 + compra2 + compra3)
media = int(soma / 3)
dobro = int(media *2)

if(soma > dobro):
    print ("verdadeiro")

if(soma < dobro):
    print("falso")