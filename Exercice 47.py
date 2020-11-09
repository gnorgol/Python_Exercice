def mots_communs(T1,T2):
    resultat = []
    T1 = T1.split()
    T2 = T2.split()

    for each in T1:
        if each in T2:
            resultat.append(each)
    return resultat
T1 = "Python est un langage de programmation"
T2 = "Python est orienté objet"
print(mots_communs(T1,T2))