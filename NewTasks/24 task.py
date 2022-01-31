#24. В заданном списке вещественных чисел 
# найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.uniform(0,10))
    return list

def FractionalPart (list):
    new_list = []
    for i in range(len(list)):
        new_list.append(round((list[i]%1), 2))
    return new_list

test_list = Filling(5)
print(test_list)

new_list = FractionalPart(test_list)
print(new_list)

print(f'{max(new_list)} - {min(new_list)} = {max(new_list)-min(new_list)}')


