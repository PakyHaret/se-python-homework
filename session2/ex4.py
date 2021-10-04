"""
    Ex. 4: Modificati urmatoarea bucata de cod astfel incat
    la rulare, lista rezultata sa fie [1, 2, 2, 3, 4, 5]
"""

# In variabila t1 vom stoca un tuplu cu 2 elemente, 1 si 2
# iar in variabila t2 vom stoca un tuplu cu 3 element 3, 4, 5
t1 = (1, 2)
t2 = (3, 4, 5)

# Rezolvare:
l1 = list(t1) + list(t2)

# Afisam lista
print(l1)