#11. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

n = int(input('Введите число элементов: '))
# 1
def Filling(n):
    list = []
    for i in range(0,n):
        list.append((-3)**i)
    return list

print(Filling(n))

# 2

my_list = [(-3)**i for i in range(n)]
print(my_list)
