import random

def rock_paper_scissors():
    choices = ["камінь", "ножиці", "папір"]
    user_choice = input("Введіть свій вибір (камінь, ножиці, папір): ").strip().lower()
    
    if user_choice not in choices:
        print("Невірний вибір! Будь ласка, введіть одне із значень: камінь, ножиці, папір.")
        return  # Завершуємо функцію, якщо введення некоректне

    computer_choice = random.choice(choices)
    print(f"Вибір комп'ютера: {computer_choice}")

    if user_choice == computer_choice:
        print("Нічия!")
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        print("Ви виграли!")
    else:
        print("Комп'ютер виграв!")

# Запускаємо гру
rock_paper_scissors()
