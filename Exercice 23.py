s = input("Saisir une nom de fichier : ")
resulat = ""
prendre = 0
for each in s :
    if each == ".":
        prendre = 1
    if prendre == 1:
        resulat = resulat + each
print(str("L'extension du fichier est "+resulat))