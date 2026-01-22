class Student:
    def __init__(self,age,name,grades,classes):
        self.age = age
        self.name = name
        self.grades = grades
        self.classes = classes

    def display(self):
        print(f'name:{self.name}\nage:{self.age}\nclasses:{self.classes}\nGrades:{self.grades}')
student1 = Student(13,'Yusuf Javaid',"A*",'math, computer science')
student1.display()
