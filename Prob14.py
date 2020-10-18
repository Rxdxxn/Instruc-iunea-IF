n=int(input("dati numarul lui Ion:"))
if (n%4==0):
    print("Ion va fi in casuta cu numarul:", n//4)
elif (n%4)==1:
    print("Ion va fi in casuta cu numarul:",round(n/4)+1)
elif (n%4)==2 or (n%4)==3 :
    print("Ion va fi in casuta cu numarul:",round(n/4))
