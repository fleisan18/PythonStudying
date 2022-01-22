#23. Показать таблицу квадратов чисел от 1 до N
import random

n = random.randint(-10,10)
print(f'n = {n}')

def TableOfQuarters(n):
    if n<0:
        n = -n
    for i in range(n):
        print(f'{i}^2 = {i**2}')

TableOfQuarters(n)
