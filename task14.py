class Student:
    def __init__(self, name, surname, age, speciality):
        self.name = name
        self.surname = surname
        self.age =age
        self.speciality = speciality

    def student_info(self):
        print(self.name, "-", self.surname, ",", self.age, "лет,", self.speciality)


Student = Student("Юлия", "Абрамова", 19, "Журналистика")

Student.student_info()
