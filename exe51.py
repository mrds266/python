peso= int(input("Fale o seu peso  "))



print("[1] Mercurio")
print("[2] Venus")
print("[3] Marte")
print("[4] Jupiter")
print("[5] Saturno")
print("[6] Urano")
r= int(input(""))












match r:
    case 1:
        Mercurio =int(peso * 0.37)
        print("Se você estivesse no planeta Mercurio você pesaria "+Mercurio)
    case 2:
        Venus  =int(peso * 0.88)
        print("Se você estivesse no planeta Venus você pesaria "+Venus)
    case 3:
        Marte  =int(peso * 0,38)
        print("Se você estivesse no planeta Marte você pesaria "+Marte)
    case 4:
        Jupiter  =int(peso * 2.64)
        print("Se você estivesse no planeta Jupiter você pesaria "+Jupiter)
    case 5:
        Saturno =int( peso *1.15)
        print("Se você estivesse no planeta Saturno você pesaria "+Saturno)
    case 6:
        Urano  =int(peso * 1.17)
        print("Se você estivesse no planeta Urano você pesaria "+Urano)