class TableMultiplication :
    def __init__(self,multiple):
        self.start = 0
        self.multiple = multiple
    def prochain(self):
        self.start = self.start + 1
        return self.start*self.multiple


tab = TableMultiplication(3)
print(str(tab.prochain()))
print(str(tab.prochain()))
print(str(tab.prochain()))
print(str(tab.prochain()))