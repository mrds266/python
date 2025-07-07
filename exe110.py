n1 = int(input("Digiteum numero "))
n2 = int(input("Digiteum numero "))

soma = int(0)
sub = int(0)
mul = int(0)
divi = int(0)

print("qual operação ele quer:")
print("[1] Adição ")
print("[2] Subtração ")
print("[3] Multiplicação ")
print("[4] Divisao ")
ope = int(input(""))

if(ope == 1 ):
    soma = n1 + n2
    print(f"A soma dos numeros é {soma}")
if(ope == 2 ):
    sub = n1 - n2
    print(f"A subtração dos numeros é {sub}")
if(ope == 3 ):
    mul = n1 * n2
    print(f"A multuplicação dos numeros é {mul}")
if(ope == 4 ):
    divi = n1 / n2
    print(f"A divisao dos numeros é {divi}")



























