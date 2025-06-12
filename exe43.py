idade1 = int(input("fale sua idade  "))
idade2  = int(input("fale sua idade  "))

mirim = int(0)
infantil = int(0)
jovem = int(0)
adulto = int(0)


if(idade1 == 9 and idade2 == 9):
    print("mirim")
    print("infantil")
    hora = int(input("Qual será o horario da luta"))
    print("Está marcado a luta de uma pessoa com" + idade1 + "anos e outra pessoa com" +idade2+ "anos na hora" +hora)
else:
    print("Luta cancelada")
if(idade1 > 10 and idade1 < 14 and idade2 > 10 and idade2 < 14):
    print("infantil")
    hora = int(input("Qual será o horario da luta"))
    print("Está marcado a luta de uma pessoa com" + str(idade1)  + "anos e outra pessoa com" +str(idade2)+ "anos na hora" +str(hora))
else:
    print("Luta cancelada")
if(idade1 > 15 and idade1 < 18 and idade2 > 15 and idade2 < 18):
    print("jovem")
    hora = int(input("Qual será o horario da luta"))
    print("Está marcado a luta de uma pessoa com" + str(idade1)  + "anos e outra pessoa com" +str(idade2)+ "anos na hora" +str(hora))
else:
    print("Luta cancelada")
if(idade1 > 19 and idade1 < 24 and idade2 > 19 and idade2 < 24):
    print("adultol")
    hora = int(input("Qual será o horario da luta"))
    print("Está marcado a luta de uma pessoa com" + str(idade1) + "anos e outra pessoa com" + str(idade2)+ "anos na hora" +str(hora))


else:
    print("Luta cancelada")

