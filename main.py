class Animal:
    def __init__(self, name , species, legs):
        self.name = input("name: ")
        self.species = "animal"
        self.legs = 4

    def voice(self):
        print("voice")

    def walking(self):
        print("Animal il walking")


class Dog(Animal):
    breed = "bulldog"

    def bark(self, bark):
        self.bark = "bark"


class Bird(Animal):
    wingspan = 50

    def __init__(self, name, wingspan):
        self.name = "Kiwi"
        self.wingspan = 50

dog = Dog("Bulldog")
bird = Bird("Kiwi")
d = Dog
b = Bird
d.bark()
b.wingspan()

