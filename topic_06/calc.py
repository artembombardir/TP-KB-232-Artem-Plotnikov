# calc.py
from operations import get_numbers, select_operation
from functions import log_to_csv

def main():
    print("Вітаємо у програмі 'Калькулятор'")
    while True:
        operation = select_operation()   # Вибір операції
        a, b = get_numbers()             # Введення чисел для операції

        try:
            result = operation(a, b)     # Виконання обраної операції
            print(f"Результат: {result}")
            log_to_csv(operation.__name__, a, b, result)
        except ValueError as e:
            print(e)

        next_calculation = input("Бажаєте виконати іншу операцію? (так/ні): ")
        if next_calculation.lower() != 'так':
            print("Дякуємо за використання калькулятора!")
            break

if __name__ == "__main__":
    main()
