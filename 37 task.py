#37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]
import random

def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-100,100))
    return list

def FindingFromSegment (list):
    count = 0
    for i in list:
        if 10<=i<=99:
            count+=1
    return count

filled_list = Filling(123)
print(filled_list)

print(f'Количество чисел из отрезка = {FindingFromSegment(filled_list)}')