def calculator():
    try:
        # Введення чисел користувачем
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operation = input("Введіть операцію (+, -, *, /): ")

        # Виконання операції
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        else:
            # Невідома операція
            raise ValueError("Невідома операція")

    except ValueError as ve:
        print(f"Помилка введення: {ve}. Будь ласка, введіть коректні дані.")
    except ZeroDivisionError as zde:
        print(f"Помилка: {zde}")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
    else:
        # Виконується, якщо не сталося жодної помилки
        print(f"Результат операції: {result}")
    finally:
        print("Програма завершила обробку операції.")

# Викликаємо функцію
calculator()
