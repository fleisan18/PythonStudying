#21. Программа проверяет пятизначное число на палиндромом.

a = input('Введите пятизначное число')

index = 0
def Palindrom(a):
    while index< len(a)//2:
        if a[index] == a[len(a)-index-1]:
            index=+1
        


