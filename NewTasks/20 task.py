#20. Определить, присутствует ли в заданном списке строк, некоторое число 

test_list = ['ac', '3', 'ghjf', '345']
test_number = input('Введите разыскиваемое число: ')

# 1
def SearchNumber(list, wanted_number):
    for i in list:
        finding = i==wanted_number
        if finding:
            break
    return finding


# 2
def SearchNumber2 (list, wanted_number):
    return list.count(wanted_number) > 0


print(SearchNumber(test_list, test_number))
print(SearchNumber2(test_list, test_number))