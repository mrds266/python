contador = int(0)
h = int(0)
m = int(0)
cont = int(0)

for contador in range(0,4,1):
    idade = int(input("fale sua idade  "))
    sexo = str(input("fale seu sexo  "))

    if(idade > 10 ):
        cont = cont + 1
    if(sexo == "h"):
        h = h + 1
    if(sexo == "m" and idade < 20):
        m = m + 1

print(f"Pessoas Com mais de 10 anos {cont}")
print(f"Quantidade de homens {h}")
print(f"Quantidade de mulheres {m}")