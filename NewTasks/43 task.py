# 43. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]



import random
# def Filling_1(length):
#     list = []
#     for i in range(length):
#         list.append(random.randint(-10,10))
#     return list

def UniqueElements_1 (my_list):
    results = []
    for i in my_list:
        if my_list.count(i) == 1:
            results.append(i)
    return results

def Filling_2(length):
    return [random.randint(-10,10) for i in range(length)]

def UniqueElements_2 (my_list):
    return [i for i in my_list if my_list.count(i) == 1]

# test_list = Filling_1(15)

test_list = Filling_2(15)
print(test_list)

print(UniqueElements_2(test_list))


