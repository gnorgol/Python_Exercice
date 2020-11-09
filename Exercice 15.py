n = int(input("saisir un nomrbe n :"))
j=0
for i in range(1,n+1):
    if(n%i==0):
        j=j+1

if (j==2 or n == 1):
    print("le nombre est premier")
else :
    print("le nombre n'est pas premier")


