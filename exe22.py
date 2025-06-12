anos = int(input("qunatos anos você tem? "))
ingles = str(input("Você fal inglês? "))

if(ingles == "sim"):
    print("verdadeiro")
if(ingles == "sim" and anos >= 25):
    print("verdadeiros")
if(anos >= 25 and ingles == "não"):
    print ("falso")
