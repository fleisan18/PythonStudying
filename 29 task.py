#29. Написать программу вычисления произведения чисел от 1 до N
n = int(input('Введите число: '))

def Factorial(n):
    if n == 0:
        return 1
    return Factorial(n-1) * n

print(Factorial(n))

