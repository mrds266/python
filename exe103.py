cont = int(0)
conta = int(input("Quanto de dinheiro você tem conta  "))
import random

s = random.randint(1,1)
cont= int(0)
dobre = int(0)
pede = int(0)
for cont in range (9999):
    
    valor = int(input("Qual valor quer apostar? "))
    total = valor
    
    print("Qaul e cor você quer?")
    print("[1]Vermelhor [2]Branco [3]Preto")
    cor = int(input(""))
            
    
    
    if(s == 1 and cor ==1):
            dobre= valor *2
            print(f"venceu {dobre}")
            para = str(input("quer para? "))
            if(para == "sim"):
                break
    if(s == 2 and cor ==2):
            dobre= valor *14
            print(f"venceu {dobre}")
            para = str(input("quer para? "))
            if(para == "sim"):
                
                break
    if(s == 3 and cor ==3):
            dobre=valor *2
            print(f"venceu {dobre}")
            para = str(input("quer para? "))
            if(para == "sim"):
                
                break
    else:
        pede =valor - valor
        print(f"venceu {dobre}")
        para = str(input("quer para? "))
        if(para == "sim"):
                
                break
    

total = total + dobre
print(f"o total é {total}")
















































