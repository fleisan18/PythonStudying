#4. Найти кубы чисел от 1 до N
import random

n = random.randint(-10,10)
print(f'n = {n}')

def TableOfCubes(n):
    table = []
    if n<0:
        n = -n
    for i in range(n+1):
        table.append(i**3)
    return table

print(TableOfCubes(n))