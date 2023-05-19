class автомобиль:
    def __init__(self, brand, model, year, price):
       self.brand = brand
       self.model = model
       self.year = year
       self.price = price

    def car_info(self):
        print(self.brand, "-", self.model, ",", self.year, ",", self.price)


автомобиль = автомобиль("Toyota", "Highlander", 2015, 2200000)
автомобиль.car_info()