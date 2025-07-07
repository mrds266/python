import random

s = random.randint(0,4)

cont = int(0)


for cont in range (9999):

        print("qual você escolhe? ")
        print("[0] pedra ")
        print("[1] papel ")
        print("[2] tesoura")
        print("[3] lagarto")
        print("[4] spock")
        es = int(input("qual você escolhe? "))  



                 #X
        if(es == s):
            print("x")
                #pedra 
        if(es == 0 and s == 1):
              print("Você pedeu")

        if(es == 0 and s == 4):
              print("Você pedeu")

        if(es == 0 and s == 2):
              print("Você venceu")
        
        if(es == 0 and s == 3):
              print("Você venceu")
                
                
                #papel
        if(es == 1 and s == 2):
              print("Você pedeu")
        if(es == 1 and s == 3):
              print("Você pedeu")
        
        if(es == 1 and s == 0):
              print("Você venceu")
        if(es == 1 and s == 4):
              print("Você venceu")        
                
                
                #tesoura
        if(es == 2 and s == 0):
              print("Você pedeu")
        if(es == 2 and s == 4):
              print("Você pedeu")

        if(es == 2 and s == 1):
              print("Você venceu")
        if(es == 2 and s == 3):
              print("Você venceu")
           
           
           
           
            #lagarto
        if(es == 3 and s == 1):
              print("Você pedeu")
        if(es == 3 and s == 4):
              print("Você pedeu")

        if(es == 3 and s == 0):
              print("Você venceu")
        if(es == 3 and s == 2):
              print("Você venceu")
            
            
            #spock
        if(es == 4 and s == 2):
              print("Você pedeu")
        if(es == 4 and s == 0):
              print("Você pedeu")

        if(es == 4 and s == 3):
              print("Você venceu")
        if(es == 4 and s == 1):
              print("Você venceu")























