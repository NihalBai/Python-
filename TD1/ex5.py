
def m_saisir():
    NCIN = input("Entre NCIN :")
    NOM =  input("Entre Nom :")
    Prenom = input("Entre Prenom :")
    Age = input("Entre Age :")
    DECISION = input("Entre DECISION (admis, refusé, ajourné) :")
    fich = open("concours.txt","a")
    lign = NCIN + ";" +NOM+";" +Prenom+";"+Age+";"+DECISION
    fich.write(lign)
   
def saisir(listeC):
    f =open("concours.txt","w")
    for cle,val in listeC.items():
        ligne = cle+";"+val[0]+";"+val[1]+";"+str(val[2])+";"+val[3]+"\n"
        f.write(ligne)
    f.close()

def admis():
    f =open("concours.txt","r")
    f2 = open("admis.txt","w")
    for ligne in f:
        if len(ligne) == 1:
            break
        l = ligne.split(";")
        if l[4].strip() == "admis":
            f2.write(ligne)
    f.close()
    f2.close()

def attente():
    f = open("admis.txt","r")
    f2 = open("attente.txt","w")
    for ligne in f:
        if len(ligne) == 1:
            break
        l = ligne.split(";")
        if int(l[3]) > 30:
            ligne2 = l[0] +":"+l[1]+";"+l[2]+"\n"
            f2.write(ligne2)
    f.close()
    f2.close()