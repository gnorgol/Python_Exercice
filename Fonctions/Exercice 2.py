def g(nb):
    generate = ["a","b","c","d","e"]
    resultat = g2(nb,generate)
    return resultat
def g2(nb,generate):
    generate2 = []
    for each in generate :
        for i in range(nb):
            generate2.append(each)
    return generate2
nb = int(input("Quelle est votre nombre : "))
print(g(nb))

