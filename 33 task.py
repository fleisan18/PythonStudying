#33. Задать массив из 12 элементов, заполненных числами из [0,9]. 
# Найти сумму положительных/отрицательных элементов массива

import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(0,9))
    return list

def SumOfPozitive (list):
    sum = 0
    for i in list:
        if i > 0:
            sum+=i
    return sum

def SumOfNegative (list):
    sum = 0
    for i in list:
        if i < 0:
            sum+=i
    return sum

filled_list = Filling(12)
print(filled_list)

print(f'Сумма положительных чисел = {SumOfPozitive(filled_list)}')
print(f'Сумма отрицательных чисел = {SumOfNegative(filled_list)}')






