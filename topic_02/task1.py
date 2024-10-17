def ask_parameters():
    a = float(input("Введіть значення a: "))
    b = float(input("Введіть значення b: "))
    c = float(input("Введіть значення c: "))
    return a, b, c

def find_discriminant(a, b, c):
    discriminant = b**2 - 4 * a * c
    return discriminant

def find_roots(a, b, c):
    discriminant = find_discriminant(a, b, c)
    
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Корінь рівняння: x = {x}")
    else:
        print("Рівняння не має дійсних коренів.")

a, b, c = ask_parameters()

find_roots(a, b, c)
