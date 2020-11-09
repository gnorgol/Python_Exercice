s ="Pyhon est un langage de programmation"
s = s.split()
premier = s[0]
dernier = s[len(s)-1]
s[0]=dernier
s[len(s)-1] = premier
s = " ".join(s)
print(s)
