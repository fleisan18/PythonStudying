from re import L


print('Hello')

#Переменные  и типы данных
#int, float, boolean, str, list...

value = None
a = 123
b = 1.23
s = 'hello world'

print(a) #вывод
print(b)
print(s)

#print(type(value))
#print(type(a))
#print(type(b))

print(a,b,s)
print(a,b,s, sep=' - ')
print('{} - {} - {}'.format(b,s,a))
print(f'{a} - {b} - {s}')

f = True
print(f)

list =[1,2,3,'hello',True]
print(list)

#Ввод и вывод данных
#print('Введите а')
#a = int(input())
#print('Введите b')
#b = int(input())

#print(f'a + b = {a+b}')

#Арифметические операции
#+, -, *, /, %, //, **

a = 1.3256666
b = 3
c = round(a*b, 8)
print(c)

#Логические операции
#>, >=, <, <=, ==, !=
#not, and, or, - не путать с &, |, ^
#is, is not, in, not in
#gen

a = 1<4 and 5>2
print(a)

f = [1,2,3,4]
print(f)
print(not 2 in f)

is_odd = not f[0] % 2 
print(is_odd)

#Управляющие конструкции
#if, if-else

#a = int(input('a = '))
#b = int(input('b = '))
#if a>b:
#    print(a)
#else:
#    print(b)

#while

orig = 23
inverted = 0
while orig !=0:
    inverted = inverted * 10 + (orig % 10)
    orig //= 10
print(inverted)

#for

list = [1,2,3,4,5]
for i in list:
    print(i**2)

for i in range(5, 10, 2):
    print(i)

text = 'съешь еще этих мягких французских булок'

print(len(text))                  #39
print('еще' in text)              #True
print(text.replace('еще', 'ЕЩЕ')) #съешь ЕЩЕ этих мягких французских булок

print(text[-5])                   #б
print(text[:])                    #съешь еще этих мягких французских булок
print(text[:2])                   #съ

#Списки

ran = range(1,5)
print(type(ran))

numbers = list(ran)
print(type(numbers))