time = ["time0","time1","time2","time3","time4","time5","time6","time7","time8","time9",]
cont = int(0)

for cont in range(0,5,1):
    print(time[cont] + "=>")

for cont in range(5,10,1):
    print(f"{time[cont]} =-=")

for cont in range(0,10,1):
    print(time[cont] + "=>",end="")