class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Student("John", 13)
p1.myfunc()

class Course:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    
    def myfunc(self):
        print("This course is " + self.name)

p2 = Course("Geometry", "hard")
p2.myfunc()