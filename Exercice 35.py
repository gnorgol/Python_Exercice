s=input("Saisissez votre texte : ")
s=s.split()
list=[]
for i in s :
    if i not in list:
        list.append(i)
        print("La fréquence d'apparition de",i,"est" ,s.count(i))