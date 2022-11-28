from arene import Arene
from de import De

de_1 = De()
de_2 = De()
de_1.valeur = 1
de_2.valeur = 2
my_dict = {(1, 2): de_1, (3, 2): de_2 }
print(my_dict)

emplacement_liste = []
for emplacement in list(my_dict.keys()):
    de = my_dict[emplacement]
    if de.valeur == 1:
        emplacement_liste.append(emplacement)
        print(emplacement_liste)
for emplacement in emplacement_liste:
    my_dict.pop(emplacement)

print(my_dict)