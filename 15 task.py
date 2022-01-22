from random import random
import random
# 15.Дано число. Проверить кратно ли оно 7 и 23

a = random.randint(1,99)
print(f'a = {a}')

def f(x):
    return a%7==0 and a%23==0

print(f(a))