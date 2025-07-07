
def comeca():
    numero = int(input("Digite um numero  "))
    PouN(numero)
    
def PouN(numero):
    if(numero >0 ):
        print("P")
    if(numero < 0):
        print("N")
    if(numero == 0):
        print("O")