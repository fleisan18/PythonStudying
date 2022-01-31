#32. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

import random
def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

def UniqueElements (my_list):
    results = []
    for i in my_list:
        if my_list.count(i) == 1:
            results.append(i)
    return results

test_list = Filling(15)
print(test_list)

print(UniqueElements(test_list))
