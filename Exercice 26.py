s = input("Entrez une phrase : ")
s = list(s)
s[0] = "a"
i = 0
for each in s :
    if (each == " "):
        s[i+1] = "a"
    i = i+1
s = "".join(s)
print(s)