def InsertEtoile(s) :
    resultat = ""
    for each in s:
        resultat = resultat + each + "*"
    return resultat

s = "Python"
print(InsertEtoile(s))
