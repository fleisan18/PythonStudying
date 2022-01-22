#17. По двум заданным числам проверять является ли одно квадратом другого

first_num = 4
second_num = 16
def Square(a, b):
    return a==b**2

print('Второе число - квадрат первого?')
result = Square(first_num, second_num)
print(result)

print('Первое число - квадрат второго?')
result = Square(second_num, first_num)
print(result)