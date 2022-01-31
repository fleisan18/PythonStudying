#13. Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.
from collections import Counter
import collections

#1

first_line = input('Введите 1 строку: ')
second_line = input('Введите 2 строку: ')

count = collections.Counter(first_line)
print(f'{count[second_line]} вхождений в {first_line}')

#2

def NumberOccurrences (first_line, second_line): 
    count = 0
    for i in first_line:
        if i == second_line:
            count+=1
    return count

print(NumberOccurrences(first_line, second_line))

#3
print(f'Кол-во вхождений: {first_line.count(second_line)}')

