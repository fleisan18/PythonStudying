#31. Задать массив из 8 элементов и вывести их на экран

import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

print(Filling(8))