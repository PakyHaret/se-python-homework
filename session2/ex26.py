"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""
#Rezolvare:
x = input().split(",")

for element in x:
    if element != "exit":
        if int(element) % 2 == 0:
            print("True")
        else:
            print("False")
