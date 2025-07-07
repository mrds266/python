contador = int(0)
joao = int(0)
i = int(0)
for contador in (0,9999,1):
    nome = str(input("fale seu nome  "))
    idade = int(input("fale sua idade "))

    if(nome == "joão" and idade > 35):
        break
    if(contador > 3):
        print("bloqueado")
        break
    if(nome != "joão"):
        joao = joao + 1
        break
    if(idade < 35):
        i = i + 1
        break
print(f"tentativas de nomes {joao} tentativas de idade {i}")
