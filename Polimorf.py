class Animal:
    head = 1
    legs = 4
    tail = 1
    def voice(self):
        print("Произносит голос")

class Dog(Animal):
    def voice(self):
        print("Gav-gav")

class Cow(Animal):
    def voice(self):
        print("Muuuuuu")

class Cat(Animal):
    def voice(self):
        print("Miaaa")


cat1, cat2 = Cat(), Cat()
dog1, dog2 = Dog(), Dog()
cow1, cow2 = Cow(), Cow()

farm_all = [cow1, cow2, cat1, cat2, dog1, dog2]

for animal in farm_all:
    animal.voice()