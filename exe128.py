import exe128funcoes
import random
a=[0,0,0,0]
a[0] =random.randint(0,4)
a[1] =random.randint(0,4)
a[2] =random.randint(0,4)
a[3] =random.randint(0,4)

dobre = exe128funcoes.analisar3(a[2])
triplica = exe128funcoes.analisar2(a[1])
soma = int(dobre + triplica)
ve = int(soma * 3.14)

print(ve)

