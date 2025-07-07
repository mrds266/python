notas =[0,0,0,0,0,0,0]
cont = int(0)
media = int(0)
maior = int(0)
soma = int(0)
menor = int(99999999)
while (cont < 6):
    cont = cont +1 
    notas[cont]= int(input("Fale o valor da nota "))
    soma = soma + notas
    media = soma / 6
    if(notas[cont] > maior):
        maior = notas[cont]
    if(notas[cont] < menor):
        menor = notas[cont]
