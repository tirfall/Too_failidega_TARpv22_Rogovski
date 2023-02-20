from funktsioonid import *
laused=[]

while True:
    v=int(input("1 - loeme failist\n2 - salvestame failisse\n3 - Tekst helisse\n"))
    if v==1:
        laused=Loe_failist("laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause")
        laused.append(line)
        sal_failisse("laused.txt", laused)
    elif v==3:
        text=" "
        for line in laused:
            text=text+line
        #ind=int(input("Number: "))
        Heli(text,"et")
