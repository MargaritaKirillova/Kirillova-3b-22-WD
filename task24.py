class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def info(self):
        print("Сотрудник:", "", self.name, " ", "Возраст:", self.age, " ", "Размер зарплаты:", self.salary, "")

employee = Employee("Юлия Абрамова", 21, 190000)
employee.info()