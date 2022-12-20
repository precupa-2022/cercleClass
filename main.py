"""
Programme fait par Alexander Precup
Groupe: 402
Description: Objets orientées
Exercise 3 - Écrire une classe Cercle
"""

from math import pi


class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_aire(self):
        return pi * self.rayon * self.rayon

    def calculer_circonference(self):
        return 2 * pi * self.rayon


c = Cercle(10)
c_aire = c.calculer_aire()
c_circonference = c.calculer_circonference()

print(f"Aire circle : {c_aire}")
print(f"Circonference circle : {c_circonference}")
