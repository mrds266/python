velocidade = int(input("Qual e a velocidade"))
multa = int(0)
eceso = int(velocidade - 80)

if(velocidade <= 80):
    print("velocidade segura")
if(eceso > 0 and eceso < 20):
    multa = 150+5*eceso


if(eceso > 21 and eceso < 80):
    multa =250+10*eceso


if(eceso > 81 and eceso > 200):
    multa = 500 + 20 *eceso


print("limite de celocidade exe=cedida. Sua meulta é " + str(multa) + " reias")


