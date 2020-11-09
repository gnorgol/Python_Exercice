s = input("Saisir une chaine de caractères : ")

i = len(s)
resulat = ""
while (i != 0):
    resulat = resulat + s[i-1]
    i=i-1
print(resulat)