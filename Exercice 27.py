s = input("Saisir une phrase: ")
s = s.split()
resultat = ""
for each in s:
    if(len(resultat)<len(each)):
        resultat = each


print("le mot le plus long est " + resultat)