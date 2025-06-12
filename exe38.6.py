tempo = int(input("fale o tempo da viajem "))
velicidade = int(input("fale o velocidade "))

distacia = int(tempo * velicidade)
litros = int(distacia / 12)

print("litros usados " + str(litros))