"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un string aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
#Rezolvare:
import random
import string

x = int(input())

random_string = "".join(random.choices(
    string.ascii_letters + string.digits, k=x))

print(random_string)
