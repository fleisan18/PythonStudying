#35. Определить, присутствует ли в заданном массиве, некоторое число
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

def IsHere (list, finding_number):
    for i in list:
        check = i == finding_number
    return check
        
filled_list = Filling(10)
print(filled_list)

print(IsHere(filled_list, 8))
