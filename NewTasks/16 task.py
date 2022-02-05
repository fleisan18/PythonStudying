# 16. Задать список из n чисел последовательности (1+1/n)**n и 
# вывести на экран их сумму

n = 10000
my_list = [(1+1/n)**n for i in range(n)]
print(my_list)
print(sum(my_list))