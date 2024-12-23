from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda s: s.name)

    def delete_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, email=None, group=None):
        for student in self.students:
            if student.name == name:
                student.update(phone, email, group)
                return True
        return False

    def get_all_students(self):
        return self.students

    def __str__(self):
        return "\n".join(str(student) for student in self.students)