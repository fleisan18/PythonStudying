# 12. Для натурального N создать словарь индекс-значение, 
# состоящий из элементов последовательности 3k + 1.


def FillingDict(k):
    dictionary = {}
    for k in range(0,k):
        dictionary[k] = 3*k+1
    return dictionary

test_dictionary = FillingDict(5)
print(test_dictionary)