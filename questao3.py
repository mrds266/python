peso = int(input("fale seu peso "))
aca = int(input("quantos dias você foi na academia nesse ano  "))
ganha = int( aca * 0.020)
perde = int( aca * 0.040)
total = int( ganha + peso - perde)

print("Você pesava " +  str(peso) + " e perdeu " + str(perde) + " kilos porem ganhou " + str(ganha) + " de massa muscular, pensando hoje "+ str(total))


