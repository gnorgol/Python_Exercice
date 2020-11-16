class Domino :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __affiche_points__(self):
        return "face A: "+str(self.a)+", face B : "+str(self.b)
    def __total__(self):
        return self.a + self.b

d = Domino(4, 6)
print(d.__affiche_points__())
x = d.__total__()
print(x)