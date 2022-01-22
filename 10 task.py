from random import random
import random


#10. Показать вторую цифру трёхзначного числа

a = random.randint(100,1000)
print(a)
second_num = a//10%10
print(second_num)