# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
#
#
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
number = int(input('Введите количество элементов в списке: '))
my_list = []
for i in range(number):
    my_list.append(random.randint(0, 10))
my_set = my_list
print(my_set)
find_number = int(input('Введите искомое число: '))
if find_number in my_list:
    print('Искомое число присутствует в  списке')
else:
    found = my_list[0]
    for item in my_list:
        if abs(item - find_number) < abs(found - find_number):
            found = item

    print(f'Ближайшее число к {find_number} в списке {my_list} является:  {found}')





