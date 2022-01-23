#26. Возведите число А в натуральную степень B используя цикл

import random

basis = random.randint(-10,10)
degree = random.randint(0,10)
print(f'a = {basis}, degree = {degree}')

def NatDegree(a,b):
    result = [a]
    a1 = a
    if b == 0:
            result = [1]
    else:
        for i in range(b-1):
            a = a1*a
            result.append(a)
    return result

print(NatDegree(basis, degree))