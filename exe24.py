numero1 = int(input("Digite o 1º numero  "))
numero2 = int(input("Digite o 2º numero  "))

soma = int(0)
media = int(0)

sm = str(input("Você quer saber a [Soma] ou a [Media]"))

if(sm == "soma"):
   soma = numero1 + numero2
   print(soma)
if(sm == "media"):
   media = numero1 = numero2 /2
   print(media)