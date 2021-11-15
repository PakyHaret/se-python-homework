"""
    Create a class "Animal". You will use this class later to extend it
    with other types of animals.

    This should be an abstract class (no functionality, only works as an
    interface for the other classes). https://docs.python.org/3/library/abc.html

    public attributes:
        - color: str
        - age: int
        - animal_type: Enum (https://docs.python.org/3/library/enum.html)

    public methods:
        - sound() - returns str
            - should return the sound the animal makes
                e.g. Dog - "woof"
        - tell_age() - returns int
            - returns the current animal age
        - age_up() - returns nothing
            - should add 1 year to the current age
        - all_implemented() - returns bool
            - this method must have a functionality, if all the methods
            above have been implemented, then this should return True,
            otherwise it should return False.

    This is an abstract class! Pay attention, this class MUST NOT have any
    functionality in it (besides all_implemented()).
    The explanations for what the methods should do are mainly for the classes
    that will extend the Animal class.
"""


from enum import Enum


class Animal:

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.animal_type = AnimalType

    def sound(self):
        if self.animal_type.name == "DOG":
            return "Ham"
        elif self.animal_type.name == "CAT":
            return "Miaw"
        elif self.animal_type.name == "CHICKEN":
            return "Codcodac"
        elif self.animal_type.name == "SNAKE":
            return "Psst"

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1

    def all_implemented(self):
        x = callable(Animal.sound)
        y = callable(Animal.tell_age)
        z = callable(Animal.age_up)
        if x == True and y == True and z == True:
            return True
        else:
            return False


class AnimalType(Enum):

    DOG = 1
    CAT = 2
    CHICKEN = 3
    SNAKE = 4
