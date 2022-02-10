# Вычислить число  c заданной точностью d
	# Пример: при d = 0.001,  = 3.141. 10-1d10-10

import math
n = int(input('Введите число слагаемых: '))

def Pi_Madhava (n):
    result = 1
    z = -1
    y = 3
    for i in range(1,n+1):
        result = result+ z**i/(y*3**i)
        y+=2
    result =result*math.sqrt(12)
    return result

print(Pi_Madhava(n))
print(math.pi)
