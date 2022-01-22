#24. Возведите число А в натуральную степень B используя цикл

import random
from unittest import result

a = random.randint(-10,10)
degree = random.randint(0,10)
print(f'a = {a}, degree = {degree}')
def NatDegree(a,b):
    result = [a]
    a1 = a
    for i in range(b):
        a = a1*a
        result.append(a)
    return result

print(NatDegree(a, degree))