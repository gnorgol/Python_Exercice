s = input("Entrez une phrase : ")
i=0
Tab = []
Tab=["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
Resultat=[0]*26
Solution=[1]*26
for i in range (0,len(N),1):
    for j in range (0,len(Tab),1):
        if (s[i]==Tab[j]):
            Resultat[j]=1

if (Solution == Resultat) :
    print ("C'est un palindrome ")
else :
    print ("C'est pas un palindrome ")
print(Resultat)
