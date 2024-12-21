from operations import Add, Subtract, Multiply, Divide

class Calculator:
    def __init__(self):
        self.operations = {
            "1": Add(),
            "2": Subtract(),
            "3": Multiply(),
            "4": Divide()
        }

    def get_numbers(self):
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Помилка: введіть коректне число.")
            return self.get_numbers()

    def select_operation(self):
        print("Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        choice = input("Ваш вибір (1/2/3/4): ")
        return self.operations.get(choice)

    def run(self):
        while True:
            operation = self.select_operation()
            if operation is None:
                print("Неправильний вибір.")
                continue
            a, b = self.get_numbers()
            try:
                result = operation.execute(a, b)
                print(f"Результат: {result}")
            except ValueError as e:
                print(e)

            next_calculation = input("Бажаєте виконати іншу операцію? (так/ні): ")
            if next_calculation.lower() != 'так':
                print("Дякуємо за використання калькулятора!")
                break

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
