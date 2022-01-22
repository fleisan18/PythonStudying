#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
from random import random
import random
a = random.randint(10,99)
print(f'a = {a}')
first_num = a//10
second_num = a%10

if first_num > second_num:
    print(first_num)
else:
    print(second_num)
