import csv
from student import Student

class FileManager:
    @staticmethod
    def load_from_csv(file_name):
        student_list = []
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.append(Student(row['name'], row['phone'], row['email'], row['group']))
            print("Data successfully loaded from file.")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty phonebook.")
        return student_list

    @staticmethod
    def save_to_csv(file_name, students):
        with open(file_name, "w", newline="") as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "group": student.group
                })
        print("Data successfully saved to file.")