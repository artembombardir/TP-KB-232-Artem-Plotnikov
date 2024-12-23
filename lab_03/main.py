from student import Student
from student_list import StudentList
from file_manager import FileManager
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.csv>")
        return

    input_file = sys.argv[1]
    student_list = StudentList()
    student_list.students = FileManager.load_from_csv(input_file)

    while True:
        action = input("Choose an action: [C]reate, [U]pdate, [D]elete, [P]rint, E[x]it: ").strip().lower()
        if action == "c":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            group = input("Enter group: ")
            student_list.add_student(Student(name, phone, email, group))
            print("New entry added.")
        elif action == "u":
            name = input("Enter the name of the student to update: ")
            phone = input("Enter new phone (leave empty to keep current): ") or None
            email = input("Enter new email (leave empty to keep current): ") or None
            group = input("Enter new group (leave empty to keep current): ") or None
            if student_list.update_student(name, phone, email, group):
                print("Entry updated.")
            else:
                print("Student not found.")
        elif action == "d":
            name = input("Enter the name of the student to delete: ")
            student_list.delete_student(name)
            print("Entry deleted if it existed.")
        elif action == "p":
            print(student_list)
        elif action == "x":
            FileManager.save_to_csv(input_file, student_list.get_all_students())
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()