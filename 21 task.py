#21. Программа проверяет пятизначное число на палиндромом.

def EnteringNumbers():
    a = input('Введите пятизначное число: ')
    while len(a) !=5:
        a = input('Введите корректно число: ')
    return a

def Palindrom(a):
    index = 0

    while index< len(a)//2:
        if a[index] == a[len(a)-index-1]:
            index=+1
        else:
            return 'Число - не палиндром'
        return 'Число - палиндром'

a = (EnteringNumbers())
print(Palindrom(a))
