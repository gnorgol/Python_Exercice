list1 = ["Voiture","Pomme","Lapin"]
list2 = ["Camion","Voiture","Orange"]
resultat = 0
for each in list1 :
    if each in list2:
        resultat = resultat + 1
print("Il y a "+str(resultat)+" valeur commune")
