# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import my_library
import math



def Squares (my_list):
    squares = [my_list[i]*my_list[len(my_list)-1-i] for i in range(math.ceil(len(my_list)/2))] 
    return squares

test_list = my_library.Filling(9)
print(test_list)

print(Squares(test_list))
