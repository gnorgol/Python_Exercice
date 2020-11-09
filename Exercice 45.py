def Nb_Maj_and_Min(L) :
    maj = 0
    min = 0
    for each in L:
        if (each.isupper()):
            maj = maj +1
        else :
            min = min +1
    return min,maj
L = input("Saisir une chaine de caractères : ")
L = list(L)
print(Nb_Maj_and_Min(L))


