cont = int(0)
import exe126funcoes
for cont in range (2):

    nu = int(input("Digite um numero"))

maior = exe126funcoes.maior(nu)
print(f"O maior numero é {maior}")
menor = exe126funcoes.menor(nu)
print(f"O menor numero é {menor}")
exe126funcoes.media(maior,menor)