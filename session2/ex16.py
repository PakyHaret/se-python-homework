"""
    Veti primi un string de la tastatura.
    Va trebui sa printati acel string, concatenat de 3 ori.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 'cmicmicmi'
"""
#Rezolvare:
x = input()
print("".join([x, x, x]))
