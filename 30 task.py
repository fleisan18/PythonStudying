# 30. Показать кубы чисел, заканчивающихся на четную цифру
from random import random
import random

list = []

def Filling(list):
    for i in range(6):
        list.append(random.randint(-10,10))
    return list

def Cube (list):
    results = []
    for i in list:
        if i % 2 == 0:
            results.append(f'{i} = {i**3}')
    return results


print(Filling(list))
print(Cube(list))