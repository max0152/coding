class Student:
    def __init__(self,name,student_id):
        self._name = name
        self._student_id = student_id
        self._grades = []
        
    def display_info(self):
        return f"Имя: {self._name} \nайди: {self._student_id}"
        
    def add_grade(self, grade):
        self._grades.append(grade)
        
    def get_average(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
        
    def get_name(self):
        return self._name
        
    def get_id(self):
        return self._student_id
        
    def get_grades(self):
        return self._grades
        
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
