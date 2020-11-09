s = input("Saisir une chaine de caractères : ")
resultat = ""
i = 1
for each in s:
    if (i%2==1):
        resultat = resultat+each
    i=i+1
print(resultat)