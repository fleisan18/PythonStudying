#14. Подсчитать сумму цифр в вещественном числе.

def SummOfFloatNumber (n):
    count = 0
    n = n.replace('.', '0')
    for i in range(len(n)):
        count+=int(n[i])
    return count
    
def IsFloat(s):
  try:
    float(s)
    return SummOfFloatNumber(s)
  except ValueError:
    return None


test_number = input('Введите вещественное число: ')
print(IsFloat(test_number))


        
