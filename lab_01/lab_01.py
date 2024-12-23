## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "group":"KB-232"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "group":"KB-232"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "group":"KB-232"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "group":"KB-232"}
]

def printAllList():
    for elem in list:
        strForPrint = (
            "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + 
            ", Email is " + elem["email"] + ", Group is " + elem["group"]
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if item["name"] == name:
            print(f"Current data: {item}")
            phone = input("Enter new phone (leave empty to keep current): ") or item["phone"]
            email = input("Enter new email (leave empty to keep current): ") or item["email"]
            group = input("Enter new group (leave empty to keep current): ") or item["group"]
            # Update the item
            item["phone"] = phone
            item["email"] = email
            item["group"] = group
            # Re-sort the list
            list.sort(key=lambda x: x["name"])
            print("Element has been updated")
            return
    print("Element was not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()
