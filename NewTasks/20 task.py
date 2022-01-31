#20. Определить, присутствует ли в заданном списке строк, некоторое число 

test_list = ['ac', '3', 'ghjf', '345']
test_number = input('Введите разыскиваемое число: ')

# 1
def SearchNumber(list, wanted_number):
    wanted_number = wanted_number
    for i in list:
        finding = i==wanted_number
        if finding:
            break
    return finding


# 2
if test_list.count(test_number) > 0:
    print(f'{test_number} присутствует')
else:
    print(f'{test_number} отсутствует')


print(SearchNumber(test_list, test_number))
