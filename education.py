class Student:
    name = ''
    student_id = 0
    
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        
    def display_info(self):
        return f"Имя: {self.name} \nайди: {self.student_id}"
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
        
class Group:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def show_students(self):
        if not self.students:
            print("группа пуста")
        else:
            for student in self.students:
                print(student.display_info())
                print()
                
misha = Student("Michael", 123)
print(misha.display_info())
group = group()
group.add_student(misha)
group.show_students()
