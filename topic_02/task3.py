def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Помилка: Ділення на нуль неможливе!"

def calculator():
    calculator = True
    while calculator:
        print("Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
    
    choice = input("Введіть номер операції (1/2/3/4): ")
    if choice == 'q':
        calculator = False
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    
    match choice:
        case '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        case '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        case '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        case '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        case _:
            print("Невірний вибір операції. Спробуйте ще раз.")

calculator()
