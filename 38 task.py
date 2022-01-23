#38. Найти сумму чисел одномерного массива стоящих на нечетной позиции
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-100,100))
    return list

def Sum (list):
    sum = 0
    for i in range(1, len(list), 2):
        sum = sum + list[i]
    return sum

filled_list = Filling(12)
print(filled_list)

print(Sum(filled_list))
