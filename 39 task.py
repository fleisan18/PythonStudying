#39. Найти произведение пар чисел в одномерном массиве. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import random
import random

list = []
def Filling(list):
    for i in range(random.randint(1,10)):
        list.append(random.randint(-10,10))
    return list

def Squares (list):
    results = []
    for i in range(len(list)//2):
        results.append(list[i]*list[len(list)-i-1])
    return results

filled_list = Filling(list)
print(filled_list)
print(Squares(filled_list))
