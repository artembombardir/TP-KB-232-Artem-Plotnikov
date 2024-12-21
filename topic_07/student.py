class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Список студентів
students = [
    Student("Artem", 22),
    Student("Andriy", 19),
    Student("Alexandr", 21)
]

# Сортування студентів за віком
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованих студентів
for student in sorted_students:
    print(student)
