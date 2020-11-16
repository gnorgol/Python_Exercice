def chiffrePorteBonheur(nb):
    verif = 0
    resultat = 0
    print(type(resultat))
    while verif != 1 :
        for each in nb:
            resultat = resultat+int(each)*int(each)
        if resultat <= 10 :
            verif = 1
            return str(resultat)
        else:
            nb = str(resultat)
            resultat = 0
            print(nb)






nb = input("Quelle est votre nombre : ")

if chiffrePorteBonheur(nb) == 1:
    print("Le nombre "+nb+" est un nombre porte bonheur")
else:
    print("Le nombre "+nb+" n'est pas un nombre porte bonheur")