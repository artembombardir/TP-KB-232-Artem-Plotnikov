def find_position(sorted_list, new_element):
    position = 0
    for elem in sorted_list:
        if new_element > elem:
            position += 1
    return position

sorted_list = [1, 3, 5, 7, 9]
print(sorted_list)

try:
    new_element = int(input("Введіть новий елемент: ")) 
except ValueError:
    print("Будь ласка, введіть коректне число.")
else:
    position = find_position(sorted_list, new_element)
    print(f"Нова позиція для елемента {new_element} у відсортованому списку: {position}")
    sorted_list.insert(position, new_element)
    print(sorted_list)

