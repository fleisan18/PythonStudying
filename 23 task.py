#23. Показать таблицу квадратов чисел от 1 до N
import random

n = random.randint(-10,10)
print(f'n = {n}')

def TableOfQuarters(n):
    table = []
    if n<0:
        n = -n
    for i in range(n+1):
        table.append(i**2)
    return table

print(TableOfQuarters(n))