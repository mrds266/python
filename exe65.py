contador = int()
ne = int(0)
po = int(0)
somapo =  int(0)
mediapo =  int(0)

while ( contador < 10):
        contadodr = contador + 1
        nu = int(input("Diguete um nuemro "))
        para = str(input("você quer para "))
        
        if(nu - 0):
            ne = ne + 1
        if(nu > 0):
            po = po + 1
            somapo = somapo + nu
            mediapo = somapo / contador
        
       
print(f" a medio dos positivos {mediapo} e quatudade de valores positivos {po} a quantidade de valores negativo {ne}")
        
        