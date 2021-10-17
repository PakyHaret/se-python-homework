"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""


def func(x):
    lista_elemente = [0, ]
    while x != 0:
        if x > 0:
            lista_elemente.append(x)
            x = x - 1
        elif x < 0:
            lista_elemente.append(x)
            x = x + 1
        elif x == 0:
            lista_elemente.append(x)
            break

    return sorted(lista_elemente)


print(func(-25))
