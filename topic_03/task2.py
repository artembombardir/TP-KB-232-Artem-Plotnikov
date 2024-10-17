def test_list_functions():
    lst = [1, 2, 3]
    print("Початковий список:", lst)

    lst.append(4)
    print("Після append:", lst)

    lst.extend([5, 6])
    print("Після extend:", lst)

    lst.insert(1, 1.5)
    print("Після insert:", lst)

    lst.remove(1.5)
    print("Після remove(1.5):", lst)

    lst.sort()
    print("Після sort():", lst)

    lst.reverse()
    print("Після reverse():", lst)

    lst_copy = lst.copy()
    print("Копія списку:", lst_copy)

    lst.clear()
    print("Після clear():", lst)

test_list_functions()
