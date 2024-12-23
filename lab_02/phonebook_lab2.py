########## Importing libraries ##########
import csv
from sys import argv

########## Global phonebook ##########
phonebook = []

########## Load from CSV ##########
def load_from_csv(file_name):
    global phonebook
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            phonebook = [row for row in reader]
        print("Data successfully loaded from file.")
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty phonebook.")

########## Save to CSV ##########
def save_to_csv(file_name):
    global phonebook
    with open(file_name, "w", newline="") as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(phonebook)
    print("Data successfully saved to file.")

########## Print all records ##########
def print_all():
    for entry in phonebook:
        print(f"Name: {entry['name']}, Phone: {entry['phone']}, Email: {entry['email']}, Group: {entry['group']}")

########## Add new record ##########
def add_new():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    group = input("Enter group: ")
    new_entry = {"name": name, "phone": phone, "email": email, "group": group}
    phonebook.append(new_entry)
    phonebook.sort(key=lambda x: x["name"])
    print("New entry added.")

########## Update record ##########
def update_entry():
    name = input("Enter the name of the student to update: ")
    for entry in phonebook:
        if entry["name"] == name:
            print(f"Current data: {entry}")
            phone = input("Enter new phone (leave empty to keep current): ") or entry["phone"]
            email = input("Enter new email (leave empty to keep current): ") or entry["email"]
            group = input("Enter new group (leave empty to keep current): ") or entry["group"]
            entry.update({"phone": phone, "email": email, "group": group})
            phonebook.sort(key=lambda x: x["name"])
            print("Entry updated.")
            return
    print("Student not found.")

########## Delete record ##########
def delete_entry():
    name = input("Enter the name of the student to delete: ")
    global phonebook
    phonebook = [entry for entry in phonebook if entry["name"] != name]
    print("Entry deleted if it existed.")

########## Main ##########
def main():
    if len(argv) < 2:
        print("Usage: python phonebook_lab2.py <input_file.csv>")
        return

    input_file = argv[1]
    load_from_csv(input_file)

    while True:
        action = input("Choose an action: [C]reate, [U]pdate, [D]elete, [P]rint, E[x]it: ").strip().lower()
        if action == "c":
            add_new()
        elif action == "u":
            update_entry()
        elif action == "d":
            delete_entry()
        elif action == "p":
            print_all()
        elif action == "x":
            save_to_csv(input_file)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
