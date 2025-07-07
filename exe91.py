conatdor = int(0)
soma = int(0)
execeso = int(0)

for contador in range (0,200,1):

    nu = int(input("Digite numero  "))
    soma = soma + nu
    execeso = int( soma -1000)
    if(soma > 1000):
        print(f"excedeu em {execeso}")
        break
















