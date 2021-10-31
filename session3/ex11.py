"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def log_output(func):
    file = open("output11.data", "a")
    file.write(f)
    file.close()

    file = open("output11.data", "r")
    print(file.read())
# decorate me


def f():
    return "CMI"
