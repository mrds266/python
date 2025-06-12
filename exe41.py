v = float(input("qunato você vendeu nesse mês?  "))
comessao = float(0)

if(v >= 22.000,00 ):
    ano = float(input("Que ano você entrou naempresa"))
    if(ano == 2):
        comessao = v * 0.03
    if(ano == 3):
        comessao = v * 0.04  
    if(ano - 2):
        comessao = v * 0.02    


print("comissão " + str(comessao))
