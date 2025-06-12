idade = int(input("fale sua idade "))
if(idade > 18):
    sexo = str(input("fale seu sexo "))
    if(sexo == "masculino"):
        naci = str(input("qual e sua nacionalidade"))
        if(naci == "br"):
            print("bem vindo soldado")
        else:
            print("não")
    else:
        print("não")
else:
    print("não")