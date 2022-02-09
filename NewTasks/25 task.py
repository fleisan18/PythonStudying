# 25. Написать программу преобразования десятичного числа в двоичное

converting_number = int(input('Введите число '))

def IntToBin(number):
    line = ''
    while number >=1:
        line = line + f'{number%2}'
        number = number//2
    return line


def Reversed(line):
    result = ''.join(reversed(line))
    return result 

print(Reversed(IntToBin(converting_number)))