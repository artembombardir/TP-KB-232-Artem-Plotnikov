import csv

LOG_FILE = 'calc_log.csv'

# functions.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("На нуль ділити не можна!")
    return a / b

def log_to_csv(operation_name, a, b, result):
    fieldnames = ['operation', 'operand1', 'operand2', 'result']
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:  # Якщо файл порожній, додаємо заголовки
            writer.writeheader()
        writer.writerow({
            'operation': operation_name,
            'operand1': a,
            'operand2': b,
            'result': result
        })