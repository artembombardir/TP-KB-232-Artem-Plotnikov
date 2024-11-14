import requests

def get_exchange_rate(currency_code):
    """Отримуємо курс валюти з API НБУ"""
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на помилки запиту
        rates = response.json()
        for rate in rates:
            if rate['cc'] == currency_code:
                return rate['rate']
        print(f"Курс для валюти {currency_code} не знайдено.")
    except requests.exceptions.RequestException as e:
        print("Помилка при з'єднанні з API НБУ:", e)
    return None

def currency_converter():
    """Функція для конвертації валюти в гривні"""
    print("Доступні валюти для конвертації: EUR, USD, PLN")
    currency = input("Введіть код валюти для конвертації (EUR, USD, PLN): ").strip().upper()
    amount = float(input("Введіть суму для конвертації: "))

    if currency not in ['EUR', 'USD', 'PLN']:
        print("Неправильний код валюти. Доступні валюти: EUR, USD, PLN.")
        return

    rate = get_exchange_rate(currency)
    if rate is not None:
        converted_amount = amount * rate
        print(f"{amount} {currency} = {converted_amount:.2f} UAH")

# Запускаємо конвертацію
currency_converter()
