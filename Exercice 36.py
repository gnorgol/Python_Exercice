s = input("Saisir une chaine de caractères : ")
count = 0
s = s.split()
for each in s:
    if (each == " "):
        del s[count]
    count = count +1
s = "".join(s)
print (s)
