def Conversion(a):
    millier = 0
    centaine = 0
    dizaine = 0
    unité =0
    while a > 1000:
        a = a - 1000
        millier += 1
    while a > 100:
        a = a - 100
        centaine += 1
    while a > 10:
        a = a - 10
        dizaine += 1
    while a > 0 :
        a = a - 1
        unité += 1
    return millier,centaine,dizaine,unité;
print("Le nombre choisis possède",Conversion(a)[0],"milliers",Conversion(a)[1],"centaines",Conversion(a)[2],"dizaines",Conversion(a)[3],"unités");
