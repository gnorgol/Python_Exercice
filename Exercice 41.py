def nombreDivisibles (liste1, n):
    listeDivisible = []
    for each  in liste1 :
        if (each % n == 1):
            listeDivisible.append(each)

    return listeDivisible;
liste1 = [1,2,3,4,5]

n = 2
resultat = nombreDivisibles(liste1,n)
print (resultat)
