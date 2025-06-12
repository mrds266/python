import random

s = random.randint(1,2)

print("Qual humorista")
print("[1] Fabio Porchat ")
print("[2] Danilo Gentili")
print("[3] Rafinha bastos")
re = int(input(""))
cidade = str(input("qual e sua cidade "))
idade = int(input("qual e sua idade "))
if(re == 2 and cidade == "São Paulo"):
    print("Tem show do Danilo Gentili")

if(re == 1 and cidade == "Araxa" and idade >= 18):
    print("Tem show do Danilo Gentili")
if(re == 3 and cidade == "Rio Grande do Sul"):
     if( s !=1):
        print("tem show do rafinha Bastos")
     else:
         print("não tem show")

