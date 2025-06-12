km = int(input("Qual e a quantidade de km percorrrido  "))
dias = int (input("quantos dias pelos quais ele foi alugado  "))
custo1 = float(dias * 60.00)
custo2 = float(km * 0.15) 
total = float( custo1 + custo2)

print("O total é " + str(total))
