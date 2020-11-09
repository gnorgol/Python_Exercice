s = input("Saisir une phrase: ")
resulat = ""
for each in s :
    if each == " ":
        resulat = resulat + each
        break
    resulat = resulat + each
print(str(resulat))