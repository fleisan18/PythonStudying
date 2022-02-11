# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
import random

data = open('17 task.txt', 'w')
data.writelines('2 \n')
data.writelines('3 \n')
data.writelines('5 \n')
data.close()

def Filling(n):
    list = []
    for i in range(n):
        list.append(random.randint(-n,n))
    return list

def Filling2 (n):
    return [random.randint(-n, n) for i in range(n)]

def Set(file):
    data = open(file, 'r')
    indexes = []
    for line in data:
        line = line.replace('\n', '')
        indexes.append(int(line))
    data.close()
    return indexes

def Multiplication(indexes, list):
    result = 1
    for i in range(len(list)):
        if i in indexes:
            result*=list[i]
    return result


# test_list = Filling(10)
test_list = Filling2(10)
print(test_list)

indexes = Set('test.txt')
print(indexes)

print(Multiplication(indexes, test_list))


