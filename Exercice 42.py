def nombreOccurences(L,x):
    i = 0
    for each in L:
        if each == x :
            i=i+1
    return i
L= [1,1,2,5,4,7,6,45,1,2,3]
x = 1
resultat = nombreOccurences(L,x)
print(resultat)