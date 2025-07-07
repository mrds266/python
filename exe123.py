import exe123funcoes
valor = int(input("Qual valor da venda? "))

print("como vai pagar? ")
print("a vista")
print("a prazo")
print("a cartão")
re = int(input(""))

if(re == 1):
    exe123funcoes.a_vista(valor)
if(re == 2):
    exe123funcoes.a_prazo(valor)
if(re == 3):
    exe123funcoes.cartao(valor)


