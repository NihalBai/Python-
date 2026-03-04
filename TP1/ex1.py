
#ex1
poules = int(input("nbr de poules"))
chiens = int(input("nbr de chiens"))
vaches = int(input("nbr de vaches"))
amis = int(input("nbr d'amis"))
ptPerdus = poules + 3*chiens + 5*vaches + 10*amis
nbrPermis = ptPerdus/100.00
payer = 200*nbrPermis
print("A payer:", end='')
if payer == 0:
    print("rien a payer")
else:
    print(payer, "euros")
           
# ex2
def dicho(a,x):
    i=0
    j=len(a)-1
    if (x-a[i]) * (x-a[j])==0:  #l element se trouve au deb la fin
        return True
    if (x-a[i]) * (x-a[j]) > 0:
        return False
    while j-i > 1:
        k = (i+j)//2
        if a[k] == x:
            return True
        if a[k] > x:
            j=k
        else:
            i=k
    return False     

