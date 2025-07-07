contador = int(0)
somaimpar = int(0)
somamu= int(0)

while (contador != 10):
        contador = contador + 1

        nu = int(input("Digite um numero  "))
      
        if(nu > 1 and nu < 500):
                
            if(nu %2==1):
                    somaimpar =somaimpar + nu
            if(nu %5==0):
                    somamu = somamu + nu
        else:
            print("burro")
            break


print(f"A soma dos numeros mutilos de 5 é {somamu} e a soma dos numeros impares {somaimpar}")



















