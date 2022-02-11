#lambda

# def f(x):
#     return x**2

# g = f
# print(type(f))
# print(type(g))

from dataclasses import dataclass


def calc1(x):
    return x+10

# print(calc1(10))

def calc2(x):
    return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc1, 10)
# math(calc2, 10)

# ------------

def sum(x, y):
    return x+y

def mylt(x,y):
    return x*y

def calc(op, a, b):
    print(op(a,b))
    # return op(a, b)

# calc(lambda x,y: x+y, 4, 5)

# list comprehension

# list = []
# for i in range(1,101):
#     # if i%2==0:
#         list.append(i)

# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1,21) if i%2==0]
# print(list)

# 1
# f = open('lecture 01.02.txt', 'r')
# data = f.read() + ' '
# f.close()

# my_list = []

# while data != '':
#     space_pos = data.index(' ')
#     my_list.append(int(data[:space_pos]))
#     data = data[space_pos+1:]


# numbers = [(i, i**2) for i in my_list if i%2==0]

# print(my_list)
# print(numbers)

# 2
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

data = '1 2 3 5 6 7 8 45 69'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x,x**2), res)
# print(res)

# map

li = [x for x in range(1,20)]
print(li)

li = list(map(lambda x: x+10, li))
print(li)

# data = list(map(int, input('Что-то введите').split()))
# print(data)

# 3
# def where(f, col):
#     return [x for x in col if f(x)]


# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x,x**2), res))
# print(res)

# filter (нельзя пройтись дважды)

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)

# 4
res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x,x**2), res))
print(res)

# zip (нельзя пройтись дважды)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,6]
salary = [111, 222, 333]

data = list(zip(users,ids, salary))
print(data)

# enumerate
data = list(enumerate(users))
print(data)

