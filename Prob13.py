n=int(input("Dati numarul lui Ion:"))
if (n<=100):
    if n%4==0:
        print ("negru")
    elif n%4==1:
        print("alb")
    elif n%4==2:
        print("rosu")
    elif n%4==3:
        print("albastru")
else:
    print("Ion nu va primi tricou")

