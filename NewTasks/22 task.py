#22. Найти сумму чисел списка стоящих на нечетной позиции
import random
def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list

def SummUneven (list):
    new_list = [list[i] for i in range(0, len(list), 2)]
    print(new_list)
    return sum(new_list)

test_list = Filling(10)
print(test_list)

print(SummUneven(test_list))