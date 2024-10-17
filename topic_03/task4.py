def find_position(sorted_list, new_element):
    for i in range(len(sorted_list)):
        if new_element < sorted_list[i]:
            return i
    return len(sorted_list) 

sorted_list = [1, 3, 5, 7, 9]

try:
    new_element = int(input("Введіть новий елемент: ")) 
except ValueError:
    print("Будь ласка, введіть коректне число.")
else:
    position = find_position(sorted_list, new_element)
    print(f"Нова позиція для елемента {new_element} у відсортованому списку: {position}")
