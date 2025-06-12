velocidade = int(input("Qual e a velocidade"))
multa = int(0)
eceso = int(velocidade - 80)
if(velocidade <= 80):
    print("velocidade segura")
if(velocidade > 81):
    multa= 450+10*eceso
    print("Limite de velocidade excedido> sua multa é" + str(multa) + "reias")