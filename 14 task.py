#14. Найти третью цифру числа или сообщить, что её нет
from random import random
import random

a = random.randint(1,1000)
print(a)

def FindThirdNumber(a):
    if a%1000//100