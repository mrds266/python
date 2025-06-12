print("Qual humorista?")
print("[1] fabio porchat")
print("[2] Danilo Gentili")
print("Rafinha bastos")
r = int(input(""))

cidade = str(input("Qual cidade você é? "))

match r:

    case 1:
        if(cidade == "araxa"):
            idade = int(input("qual e sua idade? "))
            if(idade >= 18):
                print("tem show do Fabio Porchat")
    case 2:
        if(cidade == "São Paulo"):
            print("tem show do Danilo Gentili")

    case 3:
        if(cidade == "Rio grande do sul"):
            print("tem show do Rafinha bastos")