from calculator import Calculator

def main():
    calc = Calculator()

    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == "1":
                print("Result:", calc.add(a, b))
            elif choice == "2":
                print("Result:", calc.subtract(a, b))
            elif choice == "3":
                print("Result:", calc.multiply(a, b))
            elif choice == "4":
                print("Result:", calc.divide(a, b))
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
