class Building:
    def __init__(self, nOF, bT):
        self.numberOfFloors = int(nOF)
        self.buildingType = str(bT)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(3,"Стрижи")
h2 = Building(5, "Родники")

print(h1 == h2)