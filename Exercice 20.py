s = input("Saisir une chaine de caractères : ")
i = len(s)
s = list(s)
premier = s[0]
dernier = s[len(s)-1]
s[0] = dernier
s[len(s)-1] = premier
s = "".join(s)
print(s)
