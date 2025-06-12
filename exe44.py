
dia = str(input("Que dia é hoje? "))




if(dia == "9/9/2022"):
    sabe= str(input("você sabe o que se comemora nesse dia? "))
    if(sabe == "dia do administrador"):
        senac = str(input("você sabe o que vai ter no SENAC hoje? "))
        if(senac == "sim"):
            print("então você já sabe da surpresa inesperada, nesse caso a surpresa nem é tão inesperada assim")

if(dia != "9/9/2022"):
    print("hoje é o dia de uma surpresa INESPERADA")