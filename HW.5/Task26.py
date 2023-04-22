# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(base_number, power_number):
    if (power_number == 1):
        return (base_number)
    if (power_number != 1):
        return (base_number * power(base_number, power_number - 1))
base_number = int(input("Введите число, возводимое в степень: "))
power_number = int(input("Введите его степень: "))
print( 'Число возводимое в степень =',base_number, 'его степень =',power_number, "->", power(base_number, power_number))