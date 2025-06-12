preco = float(input("Qual e o perço do produto?  "))
des = float(input("quanto e o desconto? "))
des = des / 100
des2 = float(preco * des)

print(des2)
total = float(preco - des2)


print("O pruduto custava " + str(preco) + "mas teve desconto de " + str(des) + "% por iss agora está custando " + str(total) + "reais")