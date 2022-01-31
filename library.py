import random
def Filling(length):
    list = []
    for i in range(length):
        list.append(random.randint(-10,10))
    return list