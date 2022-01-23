#42. Определить сколько чисел больше 0 введено с клавиатуры


def EnteringSet():
    set = input('Введите числа: ')
    # for i in range(len(set)):
    set = set.replace(',', '.')  
    return set

def BiggerZero(set_in_list):
    count = 0
    for i in set_in_list:
        if float(i) > 0:
            count+=1
    return count

set_in_list = EnteringSet().split()
print(set_in_list)
print(BiggerZero(set_in_list))

