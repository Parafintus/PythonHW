# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# При условии, что в номере билета 6 знаков!

print('Введите номер билета')
n = input()
summ1 = 0
summ2 = 0
for i in range(0, 3):
    summ1 += int(n[i])

for i in range(3, 6):
    summ2 += int(n[i])

if summ1 == summ2:
    print('Билет счастливый')
else:
    print("Билет НЕсчастливый")