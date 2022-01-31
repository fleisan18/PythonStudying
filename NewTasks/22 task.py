#22. Найти сумму чисел списка стоящих на нечетной позиции
import random
def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

def SummUneven (list):
    for i in range(0, len(list)-1, 1):
        removed_el = list.pop(i)
        print(removed_el)
    return sum(list)

test_list = Filling(10)
print(test_list)

print(SummUneven(test_list))