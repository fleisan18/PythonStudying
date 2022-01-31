#27. Строка содержит набор чисел. Показать большее и меньшее число

bs = [float(x) for x in input('Введите числа: ').split()]

min_value = min(bs)
max_value = max(bs)
print(bs)
print(min_value)
print(max_value)