#28. Подсчитать сумму цифр в числе
a = input('Введите число: ')

def Sum(a):
    sum = 0
    for i in a:
        sum = sum + int(i) 
    return sum

print(Sum(a))




        

