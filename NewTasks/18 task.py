# 18. Реализовать алгоритм перемешивания списка. 
import random

def Filling(n):
    list = []
    for i in range(n):
        list.append(random.randint(-n,n))
    return list

def Shuffle (list):
    for i in range(len(list)-1, 0, -1):
        j = random.randint(0, i)
        list[i], list[j] = list[j], list[i]
    return list

test_list = Filling(10)
print(test_list)

print(Shuffle(test_list))

