def toutEnMajuscule(L):
    resultat = []
    for each in L:
        resultat.append(each.upper())

    return resultat

L = ["Python", "est", "un", "langage", "de", "programmation"]
print(toutEnMajuscule(L))
