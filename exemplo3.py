print("O que você prefere")
print("[1] pastel de varne")
print("[2] pastel de queijo")
print("[3] pastel de frago")
r = int(input(""))

# escolha (r){
#    caso 1:
#        escreva("gostade carne")
#    caso 2:
#        escreva("gostade queijo")
#    caso 3:
#        escreva("gostade frango")
#
#       caso contratrio{
#        escreva("opção invalida")
#       }
#}
#

match r:
    case 1:
        print("gostade carne")
    case 2:
        print("gostade queijo")
    case 3:
        print("gostade frango")
    case _:
        print("opção invalida")

print("O que você prefere")
print("[1] pastel de varne")
print("[2] pastel de queijo")
print("[3] pastel de frago")
r = str(input(""))


match r:
    case "barne":
        print("gostade carne")
    case "queijo":
        print("gostade queijo")
    case "frango":
        print("gostade frango")
    case _:
        print("opção invalida")