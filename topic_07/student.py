class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

# Створення списку об'єктів Student
students = [
    Student("Anna", 22),
    Student("Bohdan", 19),
    Student("Iryna", 21),
    Student("Oleksii", 20),
]

# Сортування за віком (атрибут `age`)
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованого списку
for student in sorted_students:
    print(student)
