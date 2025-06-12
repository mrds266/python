valor = int(input("Digitr um valor "))
salario = int(input("Digitr o seu salario "))
mes = int (input("por quantos mêses? "))

exe = int(salario * 0.30)

parcela = float(valor / mes)

if(exe > parcela):
    print("empréstima negado")
if(exe <parcela):
    print("empréstimo")
