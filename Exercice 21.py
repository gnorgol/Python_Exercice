l = ["a", "e", "i","o","u","y"]
s = input("Saisir une chaine de caractères : ")
count = 0
for each in s :
    for i in l :
        if each == i :
            count = count+1
print(s+" possède  "+str(count)+" voyelles")