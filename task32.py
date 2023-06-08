class Student:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas

    def study(self):
        print('Школьник(ца)', self.name, '', 'учится в', self.clas, '', 'классе')


student1 = Student('Юлия', 10)

student1.study()
