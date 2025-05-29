class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):
        print(f"Make sound by, {self.name}")


dog = Animal("Mark", 10)
dog.makeSound()
