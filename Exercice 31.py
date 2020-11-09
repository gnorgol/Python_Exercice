list1 = [1,45,74,32,12,57,65,99,14,24,84,26,75]
Pair = []
Impair = []

for each in list1 :
    if (each%2 ==1):
        Pair.append(each)
    else:
        Impair.append(each)

print(Pair)
print(Impair)
