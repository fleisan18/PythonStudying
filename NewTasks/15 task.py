# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def Multiplication (n):
    list = [1, ]
    for i in range(2, n+1):
        list.append(list[i-2]*i)
    return list

print(Multiplication(5))


