
hora = int(input("fale as horas"))
mes = int(input("fale a quntidade de aulas"))
salario = float(hora * mes)

if(salario < 1.518 ):
    desconto = (0.075 * salario)
    salario = salario - desconto
if(salario > 1.518 and salario < 2.793,88):
    desconto = (0.09 * salario)
    salario = salario - desconto
if(salario > 2.793,88 and salario < 4.190,83):
    desconto = (0.12 * salario)
    salario = salario - desconto
if(salario > 4.190,83 and salario < 8.157,41):
    desconto = (0.14 * salario)
    salario = salario - desconto


print("o desconto é " + str(salario))
