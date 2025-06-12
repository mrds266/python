dis = int(input("qual a distancia da corrida do uber "))
cobre = int(0)
if(dis <= 200):
    cobre = dis * 0.35
if(dis > 200):
    cobre = dis * 0.20

ba = str(input("o bairro de destino é perigoso? "))
if(ba == "sim"):
    if(dis > 200):
        cobre = dis * 0.35*1.8
    if(dis < 200):
        cobre = dis * 0.20*1.8


print(" que o valor final da corrida para o destino escolhido é " + str(cobre)+ " reais.")