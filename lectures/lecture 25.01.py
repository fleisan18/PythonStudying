# Запись
# a - для добавления данных
# r - для чтения данных
# w - для записи данных

# colors = ['red', 'green', 'blue32']
# data = open('file.txt', 'a')
# data.writelines(colors) #без разделителей
# data.writelines('\n LINE 2 \n')
# data.write('LINE 3 \n')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2 \n')
# не нужно закрывать файл в ручном режиме

# exit() - выполнение кода до этой строки

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Функции
# import random
# import library

# print(library.Filling())

# import library as l
# print(l.Filling())

# def concatenatio(*params):
#     res = str = ''
#     for item in params:
#         res +=item
#     return res

# print(concatenatio('a', 'b', 'c', '4'))
# print(concatenatio(1,2,3)) #TypeError: can only concatenate str (not "int") to str


from cmath import e
from tkinter import E


def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib (n-2)

list = []
for i in range(1,10):
    list.append(fib(i))
print(list)

# Кортежи - неизменяемый "список"

# a = (3, 4)
# print(a)
# print(a[0])

# a[0] = 12 #TypeError: 'tuple' object does not support item assignment

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {}, g: {}, b: {}'.format(red, green, blue))
# r: red, g: green, b: blue

# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'left': 'влево',
#         'right': 'вправо',
#         'down': 'вниз'
#     }
# print(dictionary) #{'up': 'вверх', 'left': 'влево', 'right': 'вправо', 'down': 'вниз'}
# print(dictionary['left']) #влево

# for k in dictionary.keys(): 
#     print(k)
# up
# left
# right
# down

# for k in dictionary.values(): 
#     print(k)

# for k in dictionary: 
#     print(dictionary[k])

# вверх
# влево
# вправо
# вниз

# Множества

colors = {'red', 'green', 'blue'}
print(type(colors))

colors.add('gray')
print(colors) #{'gray', 'red', 'green', 'blue'}

colors.remove('red')
print(colors) #{'gray', 'green', 'blue'}

colors.clear()
print(colors) #set()

a = {1,2,3,4,5}
b = {1,2,3,6,7,8}

c = a.copy() #{1, 2, 3, 4, 5}
u = a.union(b) # {1, 2, 3, 4, 5, 6, 7, 8}
i = a.intersection(b) # {1, 2, 3}
dl = a.difference(b) # {4, 5}
dr = b.difference(a) #{8, 6, 7}

print(c,u,i,dl,dr)

s = frozenset(a) #замороженные множества

# Списки

list1 = [1,2,3,4,5]
list2 = list1

print(list1, list2)

list1[0] = 123
print(list1, list2)

list2[1] = 444
print(list1, list2)

print(list1.pop())
print(list1)

print(list1.pop(1))
print(list1)

list1.insert(2,11)
print(list1)
