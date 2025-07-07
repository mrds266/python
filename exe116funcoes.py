def lascado():
    total = int(0)
    valor = int(input("qual e sua divida "))
    tempo = int(input("qual o tampo da divida "))
    taxa = int(input("A taxa de juros"))

    juros = valor * tempo * taxa
    total = valor + juros

    print(f" O valor total  é{total}")



