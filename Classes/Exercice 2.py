class CompteBancaire :
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def affiche(self):
        return "Le solde du compte de "+str(self.nom)+" est de "+str(self.solde)+" €"
    def retrait(self,nb):
        self.solde = self.solde - nb
    def depot(self,nb):
        self.solde = self.solde + nb

compte1 = CompteBancaire('jean',1000)
compte2 = CompteBancaire('Marc')
compte1.retrait(200)
print(compte1.affiche())
compte2.depot(500)
print(compte2.affiche())