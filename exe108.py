import random

s = random.randint(0,2)

cont = int(0)


for cont in range (9999):

        print("qual você escolhe? ")
        print("[0]")
        print("[1]")
        print("[2]")
        es = int(input("qual você escolhe? "))  



                 #X
        if(es == s):
            print("x")
                #pedra 
        if(es == 0 and s == 1):
              print("Você pedeu")
        if(es == 0 and s == 2):
              print("Você venceu")
                #papel
        if(es == 1 and s == 2):
              print("Você pedeu")
        if(es == 1 and s == 0):
              print("Você venceu")
                #tesoura
        if(es == 2 and s == 0):
              print("Você pedeu")
        if(es == 2 and s == 1):
              print("Você venceu")

























