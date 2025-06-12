idade  = int(input("Qual esua idade? "))
nacionalidade  = str(input(" Qual sua nacinalidade? "))
sexo = str(input("Qual e seu sexo? "))

if(idade == 18 and nacionalidade == "br" and sexo == "masculino"):
    print("apto")
if(idade != 18 or nacionalidade != "br" or sexo != "masculino"):
    print("Não apto")
