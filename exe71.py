contador =int(0)
print("Qual tabuada você quer? ")
n =int(input())
while(contador <10):
        contador = contador + 1
        r = n * contador
        print(f"({n}) X ({contador}) X ({r})")

        if(n <=0 ):
            break