# operations.py
from functions import add, subtract, multiply, divide

def get_numbers():
    """Запитує у користувача два числа."""
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b
    except ValueError:
        print("Помилка: введіть коректне число.")
        return get_numbers()

def select_operation():
    """Запитує у користувача вибір операції та повертає відповідну функцію."""
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    choice = input("Ваш вибір (1/2/3/4): ")

    if choice == '1':
        return add
    elif choice == '2':
        return subtract
    elif choice == '3':
        return multiply
    elif choice == '4':
        return divide
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        return select_operation()
