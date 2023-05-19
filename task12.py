class Student:
    def __init__(self, name, surname, course, assessments):
        self.name = name
        self.surname = surname
        self.course = course
        self.assessments = assessments

    def average_score(self):
        print(sum(self.assessments)/len(self.assessments))

student = Student("Юлия", "Абрамова", "3 курс", [4, 5, 4])
student.average_score()
