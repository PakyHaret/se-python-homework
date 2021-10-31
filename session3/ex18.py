"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def getSum(iterable):
    if not iterable:
        return 0
    else:
        return iterable[0] + getSum(iterable[1:])


print(getSum([1, 5, 7, 12, 15]))
