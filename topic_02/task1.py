def find_roots():
    a = float(input("Введіть значення a: "))
    b = float(input("Введіть значення b: "))
    c = float(input("Введіть значення c: "))
    
    discriminant = b**2 - 4*a*c
    print(f"Дискримінант: {discriminant}")
    
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Корінь рівняння: x = {x}")
    else:
        print("Рівняння не має дійсних коренів.")

find_roots()