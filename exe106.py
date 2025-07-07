import random
so = random.randint(1,10)
multiplique = int(0)
total = int(0)
perde =int(0)
cont =int(0)
comta = int(input("Me fale o quanto de dinheiro você tem na comta  "))

while (comta != 0):
    cont = cont +1
    
    valor = int(input("Quanto você quer apostar? "))
    comta = comta - valor

    print("Qaul mutiplicador você quer?")
    print("[1] 1.1")
    print("[2] 1.3")
    print("[3] 1.6")
    print("[4] 2.0")
    print("[5] 2.5")
    ex = int(input(""))

    if(cont == 1 and ex == 1):
        multiplique = valor *1.1
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    if(cont == 1 and ex == 2):
        multiplique = valor *1.3
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    if(cont == 1 and ex == 3):
        multiplique = valor *1.6
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    if(cont == 1 and ex == 4):
        multiplique = valor *2.
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    if(cont == 1 and ex == 5):
        multiplique = valor *2.
        comta = comta + multiplique
        print(f"você venceu {multiplique}")

    if(ex == 1 and (so <= 9 or cont == 1)):
        multiplique = valor *1.1
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    elif(ex == 1 and so > 9):
        print("Pedeu")
       

    if(ex == 2 and (so <= 8 or cont == 1)):
        multiplique = valor *1.3
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    elif(ex == 2 and so > 8):
        print("Pedeu")
       

    if(ex == 3 and ( so <= 5 or cont == 1)):
        multiplique = valor *1.6
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    elif(ex == 3 and so > 5):
        print("Pedeu")

    if(ex == 4 and (so <= 4 or cont == 1)):
        multiplique = valor *2.
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    elif(ex == 4 and so > 4):
        print("Pedeu")

    if(ex == 5 and ( so <= 2 or cont == 1)):
        multiplique = valor *2.
        comta = comta + multiplique
        print(f"você venceu {multiplique}")
    elif(ex == 5 and so > 2):
        print("Pedeu")

    para = str(input("Quer para? "))

    if(para == "sim"):
        print(f"Sua conta {total}")
        print(f"O quer você pegou com as apostas {multiplique}")
        quer = str(input("Quer sacar? "))
        if(quer == "sim"):
            comta = comta + multiplique
            print(f"Sua cont {comta}")
        break
    if(comta <=0):
        print(f"Burro olha sua comta {comta}")
        break

