# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
#
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
number = int(input('Введите количество элементов в массиве: '))
my_list = []
count = 0

for i in range(number):
    my_list.append(random.randint(0,5))
print(my_list)

find_number = int(input('Введите искомое число: '))

for j in range(len(my_list)):
    if my_list[j] == find_number:
        count +=1

print(f'Искомое число повторяется раз: {count}')