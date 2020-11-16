def PowerSet(tab):
  tab = list(tab)
  reponses = []
  for i in range(2**len(tab)):
    reponse = []
    for k in range(len(tab)):
      if i & 1<<k:
        reponse.append(tab[k])
    reponses.append(reponse)
  return reponses
reponse = PowerSet(set([1,2,3]))
print(reponse)
