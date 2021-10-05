"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
#Rezolvare:
x = input()
i = 0
j = ["a", "e", "i", "o", "u"]
for litera in x.lower():
    for vocala in j:
        if litera == vocala:
            i = i + 1

print(i)
