#36. Задать массив, заполнить случайными положительными трёхзначными числами. 
# Показать количество нечетных\четных чисел

import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(100,999))
    return list

def EvenNumbers (list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count+=1
    return count

def OddNumbers (list):
    count = 0
    for i in list:
        if i % 2 != 0:
            count+=1
    return count

filled_list = Filling(10)
print(filled_list)

print(f'Количество четных элементов = {EvenNumbers(filled_list)}')
print(f'Количество нечетных элементов = {OddNumbers(filled_list)}')