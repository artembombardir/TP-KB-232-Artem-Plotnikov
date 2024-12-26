students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-232"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-232"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@gmail.com", "group": "KB-232"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@gmail.com", "group": "KB-232"}
]

def print_all_students():
    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")

def add_new_student():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    group = input("Enter student group: ")
    
    new_student = {"name": name, "phone": phone, "email": email, "group": group}
    insert_position = 0
    for student in students:
        if new_student["name"] > student["name"]:
            insert_position += 1
        else:
            break
    students.insert(insert_position, new_student)
    print("Student has been added successfully.")

def delete_student():
    name = input("Enter the name of the student to delete: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student has been deleted.")
            return
    print("Student not found.")

def update_student():
    name = input("Enter the name of the student to update: ")
    update_student = None
    for student in students:
        if student["name"] == name:
            update_student = student
            break

    if not update_student:
        print("Student not found.")
        return

    print(f"Current details - Name: {update_student['name']}, Phone: {update_student['phone']}, Email: {update_student['email']}, Group: {update_student['group']}")
    new_name = input(f"Enter new name (leave empty to keep '{update_student['name']}'): ") or update_student['name']
    new_phone = input(f"Enter new phone (leave empty to keep '{update_student['phone']}'): ") or update_student['phone']
    new_email = input(f"Enter new email (leave empty to keep '{update_student['email']}'): ") or update_student['email']
    new_group = input(f"Enter new group (leave empty to keep '{update_student['group']}'): ") or update_student['group']

    updated_student = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
    students.remove(update_student)

    insert_position = 0
    for student in students:
        if updated_student["name"] > student["name"]:
            insert_position += 1
        else:
            break

    students.insert(insert_position, updated_student)
    print("Student information has been updated successfully.")

def main():
    while True:
        choice = input("Choose an action: [C]reate, [U]pdate, [D]elete, [P]rint, e[X]it: ").lower()
        if choice == 'c':
            add_new_student()
        elif choice == 'u':
            update_student()
        elif choice == 'd':
            delete_student()
        elif choice == 'p':
            print_all_students()
        elif choice == 'x':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
