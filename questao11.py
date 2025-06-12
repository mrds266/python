peso = int(input("fale seu peso"))

print("[1] Mercurio")
print("[2] Venus")
print("[3] Marte")
print("[4] Jupiter")
print("[5] Saturno")
print("[6] Urano")
re = int(input(""))

me= int(peso * 0.37)
ve = int(peso * 0.88)
ma = int(peso * 0.38)
ju= int(peso * 2.64)
sa = int(peso * 1.15)
ur= int(peso * 1.17)

if(re == 1):
    print("seu peso em Mercurio " + str(me))
if(re == 2):
     print("seu peso em Venus " + str(ve))
if(re == 3):
         print("seu peso em Marte  " + str(ma))
if(re == 4):
        print("seu peso em Jupiter  " + str(ju))
if(re == 5):
        print("seu peso em Saturno  " + str(sa))
if(re == 6):
        print("seu peso em Urano  " + str(ur))







