"""
    Veti primi un string de la tastatura.
    Veti primi un intreg de la tastatura, x.
    Va trebui sa printati acel string, concatenat de x ori.

    exemplu:
        Veti primi: 'cmi', 5
        Veti printa: 'cmicmicmicmicmi'
"""
#Rezolvare:
y = input()
x = int(input())

first_string = y * x
print(first_string)
