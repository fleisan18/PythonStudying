#34. Написать программу замену элементов массива на противоположные
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

def Opposite (list):
    results = []
    for i in range(len(list)):
        results.append(-list[i])
    return results

filled_list = Filling(10)
print(filled_list)

print(Opposite(filled_list))