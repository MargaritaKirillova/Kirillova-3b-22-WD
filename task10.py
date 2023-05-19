class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old")


person = Person("Mary", 25)

person.say_hello()