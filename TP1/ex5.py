listeEtudiants=[]

#1
def ajouterEtudiant(CNE,nom,classe,moy_trimestre,date_naissance):
    if CNE == listeEtudiants.get("CNE"):
        print("CNE existe deja")
    jours, mois, année = date_naissance.split("/")
    etudiant={"CNE":CNE,"nom":nom,"classe":classe,"moy_trimestre":moy_trimestre,"date_naissance":{"jours":jours,"mois":mois,"année":année}}
    listeEtudiants.append(etudiant)

#2
def supprimerEtudiant():
    CNE = input("entrer le CNE de l'etudiant a supprimer: ")
    for etudiant in listeEtudiants:
        if etudiant.get("CNE") == CNE:
            listeEtudiants.remove(etudiant)
            print("etudiant supprime")
            return
    print("etudiant n'existe pas")

#3
def afficherEtudiants():
    for etudiant in listeEtudiants:
        print(etudiant) 

#4

def moyenneGenerale():
    if len(listeEtudiants) == 0:
        print("aucun etudiant dans la liste")
        return
    somme = 0
    for etudiant in listeEtudiants:
        somme += etudiant.get("moy_trimestre")
    moyenne = somme / len(listeEtudiants)
    print("moyenne generale: ", moyenne)

#5
def AfficherEtudiants():
    for etudiant in listeEtudiants:
        if etudiant.get("date_naissance").get("année") == 1996:
            print(etudiant)

