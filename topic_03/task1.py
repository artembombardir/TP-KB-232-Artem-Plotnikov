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
        return "Помилка: ділення на нуль!"

def calculator():
    while calculator:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operation = input("Введіть операцію (+, -, *, /) або 'stop' для виходу: ")

        if operation == 'stop':
            print("Вихід з калькулятора.")
            break 
        
        match operation:
            case '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            case '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            case '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            case '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            case _:
                print("Невірна операція.")
calculator()