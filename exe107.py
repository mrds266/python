cont = int(0)

desconto = int(0)
total = int(0)
aumenta = int(0)
compra = int(input("Fale o valor da compra "))


print("Forma De Pagamento")
print("[1º Pix]")
print("[2º Cartão De Debito]")
print("[3º Cartão De Credito]")
forma = int(input(""))

if(forma == 1):
    desconto = compra *0.10
    total = compra - desconto
if(forma == 2):
    desconto = compra * 0.05
    total = compra - desconto
if(forma == 3):
    vez = int(input("Em quntas vezes? "))

    if(vez <= 3):
        aumenta = compra * 0.05
        total = compra + aumenta
    if(vez > 3):
        aumenta = compra * 0.10
        total = compra + aumenta


print("valor total e " + str(total))




























