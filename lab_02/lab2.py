import sys
import csv

# Initialize the student directory
students = []

# Function to load data from a CSV file
def read_from_csv(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "group": row["group"]
                })
        print(f"Data loaded successfully from {filename}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Function to save data to a CSV file
def write_to_csv(filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to add a new student
def add_student(name, phone, email, group):
    new_student = {"name": name, "phone": phone, "email": email, "group": group}
    students.append(new_student)
    print("Student added successfully!")

# Function to delete a student
def delete_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

# Function to update a student's information
def update_student(name, new_name=None, new_phone=None, new_email=None, new_group=None):
    for student in students:
        if student["name"] == name:
            student.update({
                "name": new_name or student["name"],
                "phone": new_phone or student["phone"],
                "email": new_email or student["email"],
                "group": new_group or student["group"]
            })
            print("Student information updated successfully!")
            return
    print("Student not found!")

# Main function
def main():
    if len(sys.argv) < 2:
        print("Error: Please provide the CSV file as a command-line argument.")
        sys.exit(1)

    input_file = sys.argv[1]
    read_from_csv(input_file)

    while True:
        choice = input("Choose an action [A: Add, U: Update, D: Delete, P: Print, X: Exit]: ").upper()
        if choice == 'A':
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            email = input("Enter student email: ")
            group = input("Enter student group: ")
            add_student(name, phone, email, group)
        elif choice == 'U':
            name = input("Enter the name of the student to update: ")
            new_name = input("New name (leave blank to keep the same): ") or None
            new_phone = input("New phone (leave blank to keep the same): ") or None
            new_email = input("New email (leave blank to keep the same): ") or None
            new_group = input("New group (leave blank to keep the same): ") or None
            update_student(name, new_name, new_phone, new_email, new_group)
        elif choice == 'D':
            name = input("Enter the name of the student to delete: ")
            delete_student(name)
        elif choice == 'P':
            for student in students:
                print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")
        elif choice == 'X':
            output_file = input("Enter the filename to save data (default: output.csv): ") or "output.csv"
            write_to_csv(output_file)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
