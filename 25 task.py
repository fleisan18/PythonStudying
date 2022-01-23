#25. Найти сумму чисел от 1 до А
import random

n = random.randint(0,10)
print(f'n = {n}')

def Sum (n):
    return n*(1+n)/2

print(Sum(n))