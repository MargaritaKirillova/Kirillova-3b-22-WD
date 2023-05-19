class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def say_hello(self):
        print("My dog's name is", self.name, ",she is", self.breed, "and", self.age, "years old")


dog1 = Dog("Bonny", "dachshund", 6)

dog1.say_hello()