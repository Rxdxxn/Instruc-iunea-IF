ng = int(input("dati numarul de gaini:"))
nb = int(input("dati numarul de boabe:"))
if (nb % ng == 0):
    print("Fiecare gaina a primit ",nb // ng," boabe, iar curcanul nu a primit.")
elif (nb % ng !=0):
    if ((nb % ng) > (nb // ng)):
        print("Curcanul a primit cu ",nb % ng," boabe mai mult")
    if ((nb % ng) < (nb// ng)):
        print("Fiecare gaina a primit cu ",nb // ng," boabe mai mult")
else:
    print("au primit numar egal")