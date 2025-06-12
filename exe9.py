divida = int(input("Qual e sua divida?  "))
tempo = int(input("Qual e o tempo da divida?  "))
taxa = int(input("qual e a taxa?  "))
juros = int(divida * tempo * taxa)
total = int (divida + juros)

print("Os juros são " + str(juros) + " e o total será de " + str(total))