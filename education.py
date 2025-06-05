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
        
    def is_eligible_for_award(self):
        return False    
        
class HonorsStudent(Student):
    def is_eligible_for_award(self):
        return self.get_average() >= 90

    def display_info(self):
        info = super().display_info()
        if isinstance(self, HonorsStudent) and self.is_eligible_for_award():
            info += "\nПретендент на награду"
        return info

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
                
    def find_by_name(self, name):
        for student in self.students:
            if student._name == name:
                print(student.display_info())
                return
        print("Студент не найден")
        
    def remove_student_by_id(self, student_id):
        found = False
        for student in self.students:
            if student._student_id == student_id:
                self.students.remove(student)
                print(f"студент с айди '{student_id}' удалён.")
                found = True
                break 
        if not found:
            print(f"Студент '{student_id}' не найдено.")
            
misha1 = Student("Michael", 123)
kolya = Student("Nicolai", 124)
misha2 = Student("Michail", 126)
sveta = Student("Svetlana", 125)
group = Group()
group.add_student(misha1)
group.add_student(misha2)
group.add_student(kolya)
group.add_student(sveta)
group.show_students()
group.remove_student_by_id(125)
group.show_students()
print(misha1.is_eligible_for_award())
print(kolya.is_eligible_for_award())
