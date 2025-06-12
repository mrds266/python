idade1 = int(input("Qual e sua idade  "))
idade2 = int(input("Qual e sua idade  "))
idade3 = int(input("Qual e sua idade  "))
idade4 = int(input("Qual e sua idade  "))

maior = int(0)
menor = int(99999)


if(idade1 > maior):
    maior = idade1
if(idade2 > maior):
    maior = idade3
if(idade3 > maior):
    maior = idade3
if(idade4 > maior):
    maior = idade4

if(idade1 < menor ):
    menor = idade1
if(idade2 < menor ):
    menor = idade2
if(idade3 < menor ):
    menor = idade3
if(idade4 < menor ):
    menor = idade4

print("O mais jojem tem " + str(menor) + "anos e o masi velho tem " + str(maior) + "anos")

