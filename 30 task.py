# 30. Показать кубы чисел, заканчивающихся на четную цифру
from random import random
import random


def Filling():
    list = []
    for i in range(random.randint(1,10)):
        list.append(random.randint(-10,10))
    return list

def Cube (list):
    results = []
    for i in list:
        if i % 2 == 0:
            results.append(f'{i}^3 = {i**3}')
    return results


filled_list = Filling()
print(filled_list)
print(Cube(filled_list))