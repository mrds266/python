print("qual serie você viu no final de semana?")
print("[1] Sandman ")
print("[2] Wandinha")
print("[3] Game of Thrones")
print("[4] Dota")
print("[5] Dexter")
se = int(input(""))
Sandman  = str("")
Wandinha = str("")
Game = str("")
Dota = str("")
Dexter = str("")

match se:
    case 1:
        Sandman = "Sandman"
        print("A seria escolhida foi " + Sandman)
    case 2:
        Wandinha = "Wandinha"
        print("A seria escolhida foi " + Wandinha)
    case 3:
        Game = "Game of Thrones"
        print("A seria escolhida foi " + Game )
    case 4:
        Dota = "Dota"
        print("A seria escolhida foi " + Dota)
    case 5:
        Dexter = "Dexter"
        print("A seria escolhida foi " + Dexter)

