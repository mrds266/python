valor = int(input("fale o valor "))

print("Qual epoca do ano")
print("[1] carnaval")
print("[2] Ferias escolares")
print("[3] dia das crianças")
print("[4] black friday")
print("[5] natal")
re = int(input(""))

if(re == 1):
    valor = valor + (valor * 0.10)
    
if(re == 2):
    valor = valor + (valor * 0.20)
if(re == 3):
    valor = valor + (valor * 0.05)
if(re == 4):
    valor = valor - (valor * 0.30)
if(re == 5):
    valor = valor - (valor * 0.05)

print("O preço final em cada caso é" + str(valor))
