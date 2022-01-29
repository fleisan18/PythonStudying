#11. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

def Filling(n):
    list = []
    for i in range(0,n):
        list.append((-3)**i)
    return list

print(Filling(5))



