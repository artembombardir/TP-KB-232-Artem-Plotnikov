def test_dict_functions():
    d = {'a': 1, 'b': 2, 'c': 3}
    print("Початковий словник:", d)

    d.update({'d': 4, 'e': 5})
    print("Після update:", d)

    del d['b']
    print("Після del:", d)

    print("Ключі словника:", d.keys())

    print("Значення словника:", d.values())

    print("Пари ключ-значення:", d.items())

    d.clear()
    print("Після clear():", d)

test_dict_functions()
