valor = int(input("fale o valor da conpra "))

desconto = float(0)

if(valor > 500):
    desconto = valor - 0.05
else:
    valor = valor



print("O valor final da sua compra é " + desconto)