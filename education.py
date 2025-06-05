class Student:
    name = ''
    student_id = 0
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        return f"Имя: {self.name} \nайди: {self.student_id}"
class Group:
    def __init__(self):
        self.students = []

misha = Student("Michael", 123)
print(misha.display_info())
