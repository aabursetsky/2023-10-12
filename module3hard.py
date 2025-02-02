def calculate_structure_sum(*args):
    summa = 0
    for item in args:
        if isinstance(item, list):
            for element in item:
                summa += calculate_structure_sum(element)   # список
        elif isinstance(item, tuple):
            for element in item:
                summa += calculate_structure_sum(element)   # кортеж
        elif isinstance(item, set):
            for element in item:
                summa += calculate_structure_sum(element)   # множество
        elif isinstance(item, dict):
            for key, value in item.items():
                summa += calculate_structure_sum(key, value) # словарь
        elif isinstance(item, str):
            summa += len(item)                              # длина строки
            # print('str', summa)
        elif isinstance(item, int):
            summa += item                                   # значение числа
            # print('int', summa)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) 
