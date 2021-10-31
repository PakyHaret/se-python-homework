"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""


def next_letter(letters):
    new_string = ''.join(chr(ord(char)+1) for char in letters)
    return new_string


print(next_letter("aabbcc"))
