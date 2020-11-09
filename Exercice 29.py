s = input("Saisir une phrase: ")
s = s.split()
resultat = []
for each in s :
    if each not in resultat:
        resultat.append(each)
resultat = " ".join(resultat)
print(resultat)
