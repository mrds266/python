def abatecer(com,li):
    if(li > 20 and com == "alcool"):
        des = int(li * 0.05)
        li = li * 1.90 - des
    if(li <= 20 and com == "alcool"):
        des = int(li * 0.03)
        li = li * 1.90 - des
    if(li > 20 and com == "gasolina"):
        des = int(li *0.06)
        li = li *2.50 - des
    if(li <= 20 and com == "gasolina"):
        des = int(li *0.06)
        li = li *2.50 - des
    print(f"O valor é {li}")