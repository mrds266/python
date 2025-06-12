nota1 = int(input("fale a nota ")) 
nota2 = int(input("fale a nota "))
f = int(input("qual e sua ferquênica? "))

media = int(nota1 + nota2 * 2)

if(media >= 60 and f > 75):
    print("aprovado")
if(media > 40 and media < 60):
    print("esta de recuperação")
    r = float(input("Fale a nota de recuperação"))
    if(r <= 69.99):
        print("Reprovado")
if(media < 40):
    print(" reprovado sem direito a recuperação")