"""
    Veti primi stringuri de la tastatura, pana cand primiti stringul 'exit'.
    Va trebui sa printati o lista cu stringurile primite fara ultimul caracter
    al fiecarui string.

    Observatii:
        - lungimea stringurilor va fi intotdeauna cel putin 1

    exemplu:
        Veti primi: 'cmi', 'center', 'for', 'machines'
        Veti printa: ['cm', 'cente', 'fo', 'machine']
"""
#Rezolvare finala:

x = input().split(",")
lista_rezultate = []

for element in x:
    if element.lower() != "exit":
        lista_rezultate.append(element[:-1])

print(lista_rezultate)

