S1 = ["Voiture","Pomme","Lapin","Ordinateur","Camion"]
S2 = ["Camion","Voiture","Orange","Poulet","Lapin"]
resultat = []

for each in S1:
    if each in S2 :
        resultat.append(each)

print(resultat)