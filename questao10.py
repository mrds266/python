n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
print(" [1] soma")
print(" [2] subtração")
print(" [3] multiplicação")
print(" [4] divisão")
re = int(input(""))
soma = int()
sub = int()
mult = int()
divi = int()

if(re == 1):
    soma = n1 + n2
    print(soma)
if(re == 2):
    sub = n1 - n2
    print(sub)
if(re == 3):
    mult = n1 * n2
    print(mult)
if(re == 4):
    divi = n1 / n2
    print(divi)

