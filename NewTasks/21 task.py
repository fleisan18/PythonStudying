#21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.\

first_line = input('Введите 1 строку: ')
second_line = input('Введите 2 строку: ')

#1
def PositionSecondOccurrence (first_line, second_line): #если второе вхождение не на последнем месте
    for i in range(len(first_line)):
        if first_line[i] == second_line:
            for j in range(i+1, len(first_line)):
                if first_line[j] == second_line:
                    return j
                    break
        else:
            return None

#2
def PositionSecondOccurrence_2 (first_line, second_line): 
    if first_line.count(second_line) == 0:
        return None
    elif first_line.count(second_line) == 2:
        return first_line.index(second_line, first_line.index(second_line)+1 , len(first_line))
    

print(PositionSecondOccurrence(first_line, second_line))
print(PositionSecondOccurrence_2(first_line, second_line))

