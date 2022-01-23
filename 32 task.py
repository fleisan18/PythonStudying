#32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(0,1))
    return list

print(Filling(8))