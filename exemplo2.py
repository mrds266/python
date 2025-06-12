a = int(input("Digite um numero "))

if(a > 10):
    print("deu certo")
else:
    print("deu errado")

if( a > 10 and a < 20):
    print("deu certo1")
elif(a > 30 or a > 50):
    print("deu certo")
else:
    print("deu errado")

# inclua a bibliotaca util

import random

a = random.randint(10,20)

print(a)