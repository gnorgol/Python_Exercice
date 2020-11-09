s = input("Entrez un mot : ")
i = len(s)
resultat = ""
while (i != 0):
    resultat = resultat + s[i-1]
    i=i-1
if (resultat == s) :
    print ("C'est un palindrome ")
else :
    print ("C'est pas un palindrome ")