# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# k = 8 [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def Fibonacci (k):
    result = [0,1]
    for i in range(1, k):
        result.append(result[i]+result[i-1])
    return result


def minus_Fibonacci(k):
    result = [0,1]
    for i in range(1, k):
        result.append(result[i-1]-result[i])
    result.remove(0)
    result.reverse()
    return result


def unity_Fibon (first_func, sec_funk, k):
    result1 = first_func(8)
    result2 = sec_funk(8)
    result2.extend(result1)
    return result2

print(unity_Fibon(Fibonacci, minus_Fibonacci, 8))


