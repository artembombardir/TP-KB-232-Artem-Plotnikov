import operator

# Пріоритет операторів
OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '^': (3, operator.pow)
}

def infix_to_postfix(expression):
    """
    Перетворення інфіксного виразу в ЗПЗ (зворотний польський запис).
    """
    output = []
    stack = []

    for token in tokenize(expression):
        if token.isdigit():
            output.append(token)  # Якщо число, додаємо до виходу
        elif token == '(':
            stack.append(token)  # Відкриваюча дужка
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Видаляємо відкриваючу дужку
        elif token in OPERATORS:
            while (stack and stack[-1] in OPERATORS and
                   OPERATORS[token][0] <= OPERATORS[stack[-1]][0]):
                output.append(stack.pop())
            stack.append(token)

    # Виштовхуємо залишок операторів у стеку
    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix):
    """
    Обчислення значення виразу у ЗПЗ.
    """
    stack = []

    for token in postfix:
        if token.isdigit():
            stack.append(float(token))  # Додаємо число в стек
        elif token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            operation = OPERATORS[token][1]
            stack.append(operation(a, b))  # Виконуємо операцію

    return stack.pop()

def tokenize(expression):
    """
    Розбиває вхідний вираз на токени (числа, оператори, дужки).
    """
    import re
    return re.findall(r'\d+|[+\-*/^()]', expression)

if __name__ == "__main__":
    # Приклад використання
    expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    print("Інфіксний вираз:", expression)

    postfix = infix_to_postfix(expression)
    print("ЗПЗ:", ' '.join(postfix))

    result = evaluate_postfix(postfix)
    print("Результат:", result)