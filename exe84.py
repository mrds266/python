contador = int(0)
A = int(0)
B = int(0)
C = int(0)

for contador in (0,4,1):
    nome = str(input("fale o nome do produto  "))
    vendas = float(input("fale valo das vendas  "))
    fechar = int(input("quer fechar caixa? "))

    if(fechar == "sim"):
        break
    if(vendas > 1000,00):
        A = A + 1
    if(vendas > 500,00 and vendas < 999,99):
        B = B + 1
    if(vendas < 499,99):
        C = C + 1


print(f"pessoas que são padrão A {A}")
print(f"pessoas que são padrão B {B}")
print(f"pessoas que são padrão C {C}")


