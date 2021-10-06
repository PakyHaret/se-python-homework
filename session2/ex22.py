"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
#Rezolvare:

x = input()
sir_nou = ""
i = 0

for element in x:
    if i % 2 == 0:
        sir_nou = sir_nou + x[i].upper()
        i = i + 1
    else:
        sir_nou = sir_nou + x[i].lower()
        i = i + 1

print(sir_nou)
