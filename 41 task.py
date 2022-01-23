#41. Выяснить являются ли три числа сторонами треугольника

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

def Triangle(a,b,c):
    return a<b+c and b<a+c and c<a+b

print(Triangle(first_number, second_number, third_number))