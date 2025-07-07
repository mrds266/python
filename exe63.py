contador = int(0)
m5 = int(0)
m3 = int(0)
while (contador < 7):
    nu = int(input("Digite um numuro "))
    contador = contador + 1
    if(nu %5==0):
        m5 = m5 + 1
    if(nu %3==0):
        m3 = m3 + 1
print(f"Foram ienticados {m5} números que são múltiplos de cinco e {m3} números que são multiplo por 3.")