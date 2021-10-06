"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
#Rezolvare:
x = input()
i = 0
j = 0
lista_vocale = ["a", "e", "i", "o", "u"]

for litera in x:
    for vocala in lista_vocale:
        if litera == vocala:
            i = i + 1
    if litera != vocala:
        j = j + 1

j = j - i

print(i)
print(j)
