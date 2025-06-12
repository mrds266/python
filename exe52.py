pro = int(input("Qual e o preço so produto? "))
print("qual época do ano estamos")
print("[1] Carnaval ")
print("[2] Férias escolares ")
print("[3] Dia das Crianças ")
print("[4] Black Friday")
print("[5] Natal ")
r = int(input(""))

match r:
    
    case 1:
        ca = float(pro * 1.10)
        print("O preço final nessa data é "+ ca)
    case 2:
        fe = float(pro * 1.20)
        print("O preço final nessa data é "+ fe)
    case 3:
        diacri = float(pro * 1.02)
        print("O preço final nessa data é "+ diacri)
    case 4:
        bla = float(pro * 0.70)
        print("O preço final nessa data é "+ bla)
    case 5:
        na = float(pro * 0.95)
        print("O preço final nessa data é "+ na)










