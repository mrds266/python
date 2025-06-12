conta = int(input("quanto de dinheiro voce tem na conta "))
conpra1 = int(input("fale o valor da 1º conpra "))
conpra2 = int(input("fale o valor da 2º conpra "))
soma = int(conpra1 + conpra2)
if(conta > soma):
    print("verdadeiro")
else:
    print("falso")