def analisar(nu1,nu2,nu3):
    maior = int(0)
    menor = int(99999)

    if(nu1 > maior ):
        maior = nu1
    if(nu2 > maior ):
        maior = nu3
    if(nu3 > maior ):
        maior = nu3

    if(nu1 < menor ):
        menor = nu1
    if(nu2 < menor ):
        menor = nu2
    if(nu3 < menor ):
        menor = nu3

    print(f"O maior numero e {maior}")
    print(f"O menor numero é {menor}")