valor = int(input("fale o valor "))
desconto = int(0)

print(" 1 pix")
print(" 2 dinheiro")
print(" 3 cartão de credito")
tipo =int(input("qual e o tipo de pagamento"))
avista = str(input("A vista ? "))

juros = int (0)

if(tipo == 1 and avista == "sim"):
   desconto = valor * 0.15
   total = valor - desconto
if(tipo == 2 and avista == "sim"):
   desconto = valor * 0.15
   total = valor - desconto
if(tipo == 3):
   desconto = valor * 0.10
   total = valor - desconto
if (tipo == 4):
    pacela = int(input("em quantas pacelas? "))
    if(pacela == 2):
            total = valor / 2
    if(pacela >= 3 ):
            juros = valor * pacela
            total = valor = juros



print("valor total e " + str(total))