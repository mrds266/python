contador = int(0)

while contador <= 13:
    contador = contador + 1
    print("{} --".format(contador),end="")
    if  contador %3 == 0:
        print("PIN \n")