
pesomedio = int(78.5)
contador = int(0)
acima = int(0)
abaixo = int(0)
while (contador < 4):
    contador =contador + 1
    peso = int(input("fale seu peso "))

    if(peso > pesomedio):
        acima = acima + 1
    if(peso < pesomedio):
        abaixo = abaixo + 1
print(f"existe {acima} pessoas qie estão acima do peso médio e existe {abaixo} pessoas com peso igual ou abaixo a média")