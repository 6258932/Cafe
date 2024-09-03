cafes = [("cafea", 12, 3), ("cafeb", 10, 2), ("cafec", 8, 1), ("cafed", 9, 2), ("cafee", 11, 3),
         ("cafezero", 0, 10), ("cafe tres proche", 0.1, 11)]


class Cafe:
    def __init__(self, name, distance, qualite):
        self.name = name
        self.distance = distance
        self.qualite = qualite
        if distance == 0 or distance < 1:
            distance = 0.00001

        self.score = qualite / distance

    def __str__(self):
        print("Function __str")
        return f'{self.name} est à {self.distance} km et a une qualité de {self.qualite}'

    def __repr__(self):
        print("Function __repr")
        return f'{self.name}'

    def __eq__(self, other):
        return self.score - other.score


liste_cafes = []
for cafe in cafes:
    liste_cafes.append(Cafe(cafe[0], cafe[1], cafe[2]))

liste_cafes.sort(key=lambda x: x.score, reverse=True)
