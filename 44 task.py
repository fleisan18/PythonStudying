# 44. Найти точку пересечения двух прямых заданных уравнением 
# y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы


k1 = int(input('Введите k1 '))
k2 = int(input('Введите k2 '))
b1 = int(input('Введите b1 '))
b2 = int(input('Введите b2 '))



def Parallelism(k1,k2):
    return k1%k2==0 and k2%k1==0

def FindX(k1,k2,b1,b2):
    parall = Parallelism(k1,k2)
    res = ''
    if parall:
        return 'Прямые параллельны'
    else:
        return (b2 - b1) / (k1 - k2)

x = FindX(k1,k2,b1,b2)

def FindY(k1,x,b1):
    parall = Parallelism(k1,b1)
    res = ''
    if parall:
        return 'Прямые параллельны'
    else:
        return k1 * x + b1

print(FindX(k1,k2,b1,b2))
print(FindY(k1,x,b1))
