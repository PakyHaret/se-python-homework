"""
    Veti primi 2 numere intregi de la tastatura (x si y).
    Va trebui sa le convertiti si apoi sa printati valorea lui x la puterea y.

    exemplu:
        Veti primi: 2 si 3
        Veti printa: 8
"""
#Rezolvare:
x = int(input())
y = int(input())

print(pow(x, y))

#Se mai poate rezolva si asa:
#print(x ** y)