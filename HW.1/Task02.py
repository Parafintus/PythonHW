# Задача 2: Найдите сумму цифр трехзначного числа.
print('Введите ТРЕХЗНАЧНОЕ число: ')
# n = int(input())
# if 100 < n < 1000:
#     summ = 0
#     while n > 0:
#         x = n % 10
#         summ = summ + x
#         n = n // 10
#     print(summ)
# else:
#     print('input ERROR')

# Без цикла, при условии, что вводится трехзначное число: (ненужное закоментить!)
n = int(input())
if 100 < n < 1000:
    summ = n % 10 + (n//10) % 10 + (n//100) % 10
    print(summ)
else:
    print('input ERROR')
