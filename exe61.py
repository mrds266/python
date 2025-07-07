

contador = int(0)
somapar = int(0)
somaimpar = int(0)
while ( contador < 5 ):
        contador = contador + 1
        n = int(input("digiet um numero "))
        
        if(n %2==0):
            somapar = somapar + n
        if(n %2==1):
            somaimpar = somaimpar + n

print(f"A soma dos impares é soma {somaimpar} e a soma dos pares é {somapar} ")
