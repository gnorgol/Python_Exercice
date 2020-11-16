class Poly :
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def coeff(self):
        coeff = [self.x,self.y,self.z]
        return coeff
    def evalue(self,x):
        resultat = self.x+self.y*x+self.z*(x*x)
        return resultat

p = Poly(3,4,-2)
print(p.coeff())
print(str(p.evalue(2)))
print(list(enumerate(p.coeff())))