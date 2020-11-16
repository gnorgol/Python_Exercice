class CompteBancaire :
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde
    def __repr__(self):
        return {"compte de  ":self.nom,"solde ":self.solde}
    def retrait(self,nb):
        self.solde = self.solde - nb
    def depot(self,nb):
        self.solde = self.solde + nb

compte1 = CompteBancaire('jean',1000)
compte2 = CompteBancaire('Marc')
compte1.retrait(200)
print(compte1.__repr__())
compte2.depot(500)
print(compte2.__repr__())