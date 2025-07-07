def a_vista(valor):
    total = int(0)
    total = valor * 0.9
    print(f"O Total {total}")
def a_prazo(valor):
    total = int(0)
    total = valor * 1.1
    print(f"O Total {total}")
def cartao(valor):
    nparcela = int(input("quantas vezes? "))
    parcela = valor * 1.20/nparcela
    
    print(f"sua parcela {parcela}")
    