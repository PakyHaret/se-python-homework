"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""
#Rezolvare:
x = input()
i = []

for element in x:
    i.append(element)

print(tuple(i))
