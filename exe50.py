n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
print("[1] soma")
print("[2] subtração")
print("[3] miltiplicação")
print("[4] divisão")
r= int(input(""))
soma = int(0)
sub = int(0)
mul = int(0)
divi = int(0)
match r:
    case 1:
        soma = n2 + n1
        print(soma)
    case 2:
        sub = n1 - n2
        print(sub)
    case 3:
        mul = n2 * n1
        print(mul)
    case 4:
        divi = n1 / n2
        print(divi)





