#36. Дан список чисел. 
# Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import random
import my_library as library

def Increasing (list):
    sorted_list=[]
    r = random.randint(1,(len(list)-1)//3) 
    sorted_list.append(list[r])
    for i in range(r, len(list), r):
        if list[i] > sorted_list[-1]:
            sorted_list.append(list[i])
    return sorted_list, r

test_list = library.Filling(15)
print(test_list)

print(Increasing(test_list))


