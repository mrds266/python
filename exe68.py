
contador = int(0)
multa = int(0)
while (contador < 99999):

        usuario = str(input("Fale seu usuario "))
        senha = str(input("fale sua senha "))
                
        if(usuario != "facil" and senha != "ff"):
                    multa = multa * 2.00
                    print("errado")

        if(usuario == "facil" and senha == "ff"): 
                
                    print("acesso correto")
                    print(multa) 





