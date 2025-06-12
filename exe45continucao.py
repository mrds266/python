n1 = int(input("Digite um numero ")) 
n2 = int(input("Digite um numero "))
n3 = int(input("Digite um numero "))




if(n1 == n2 and n2 == n3):
    print("Equilatero")
elif(n1 != n2 and n2 != n3):
    print("Escaleno")
else:
    print("Ioceles")