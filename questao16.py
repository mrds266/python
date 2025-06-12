peso  = float(input("Qual e seu peso? "))
altura = float(input("Qual e sua altura? "))

imc = float(peso /(altura * altura))
pesoi = float(21.75 * (altura * altura))

if(imc < 18.5):
    print("abaixo do peso")
    print("")
if(imc >= 18.5 and imc <= 24.9):
    print("peso normal")
    print("")
if(imc >= 25 and imc <= 29.9):
    print("sobrepeso")
    print("")
if(imc >= 30 and imc <= 34.9):
    print("obesidade 1")
    print("")
if(imc >= 35 and imc <= 39.9):
    print("obesidade 2")
    print("")
if(imc >= 40):
    print("obesidade 3 ou obesidade mórbida")
    print("")
if(peso <= pesoi):
    total = float(pesoi - peso)

else:
    total = float(peso - pesoi)

