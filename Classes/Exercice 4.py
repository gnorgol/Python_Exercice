import math

class Fraction:
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    def affiche(self):
        return str(self.num)+"/"+str(self.denom)
    def __add__(self, other):
        divcommun = math.gcd(self.denom, other.denom)
        if divcommun == other.denom:
            numbis = other.num * divcommun +self.num
            denombis= other.denom * divcommun
        else:
            numbis = self.num * divcommun + other.num
            denombis = self.denom * divcommun

        return Fraction(numbis,denombis)

    def __truediv__(self, other):
        numbis = self.num / other.num;
        denombis = self.denom / other.denom;
        return Fraction(int(numbis),int(denombis))


f = Fraction(3,4)
print(f.affiche())
g = Fraction(1,2)
print(g.affiche())
r1 = f + g
print(r1.affiche())
r1 = f / g
print(r1.affiche())