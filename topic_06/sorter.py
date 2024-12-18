import csv

names = []
with open("students.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        names.append({'name': row[0], 'mark': int(row[1])})

key = input("Сортувати за 'name' чи 'mark': ").strip()

if key == 'name':
    sorted_names = sorted(names, key=lambda x: x['name'])
elif key == 'mark':
    sorted_names = sorted(names, key=lambda x: x['mark'])
else:
    print("Неправильний вибір!")
    sorted_names = []

for name in sorted_names:
    print(f"Ім'я: {name['name']}, Оцінка: {name['mark']}")
