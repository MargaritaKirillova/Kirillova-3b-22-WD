class кошка:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def cat_info(self):
        print("кошка по имени", self.name, ",", self.age, "лет", ",", self.color, "цвет")


кошка = кошка("Ласка", 5, "белый")
кошка.cat_info()