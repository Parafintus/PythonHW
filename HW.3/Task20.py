# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12
language = input('На каком языке(EN/Ru) будем играть: ')
list_ru = ('RU', 'ru', 'Ru', 'rU')
list_en = ('EN', 'En', 'en', 'eN')
if language in list_ru:
    list_ru_1 = ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т')
    list_ru_2 = ('Д', 'К', 'Л', 'М', 'П', 'У', 'д', 'к', 'л', 'м', 'п', 'у')
    list_ru_3 = ('Б', 'Г', 'Ё', 'Ь', 'Я', 'б', 'г', 'ё', 'ь', 'я')
    list_ru_4 = ('Й', 'Ы', 'й', 'ы')
    list_ru_5 = ('Ж', 'З', 'Х', 'Ц', 'Ч', 'ж', 'з', 'х', 'ц', 'ч')
    list_ru_8 = ('Ш', 'Э', 'Ю', 'ш', 'э', 'ю')
    list_ru_10 = ('Ф', 'Щ', 'Ъ', 'ф', 'щ', 'ъ')

    count_ru = 0

    word = input('Введите слово: ')
    for i in range(len(word)):
        if word[i] in list_ru_1:
            count_ru += 1
        elif word[i] in list_ru_2:
            count_ru += 2
        elif word[i] in list_ru_3:
            count_ru += 3
        elif word[i] in list_ru_4:
            count_ru += 4
        elif word[i] in list_ru_5:
            count_ru += 5
        elif word[i] in list_ru_8:
            count_ru += 8
        elif word[i] in list_ru_10:
            count_ru += 10
    print(f'Вы набрали очков: {count_ru}')

elif language in list_en:
    list_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r')
    list_2 = ('D', 'G', 'd', 'g')
    list_3 = ('B', 'C', 'M', 'P', 'b', 'c', 'm', 'p')
    list_4 = ('F', 'H', 'V', 'W', 'Y', 'f', 'h', 'v', 'w', 'y')
    list_5 = ('K', 'k')
    list_8 = ('J', 'X', 'j', 'x')
    list_10 = ('Q', 'Z', 'q', 'z')

    count = 0

    word = input('Введите слово: ')
    for i in range(len(word)):
        if word[i] in list_1:
            count += 1
        elif word[i] in list_2:
            count += 2
        elif word[i] in list_3:
            count += 3
        elif word[i] in list_4:
            count += 4
        elif word[i] in list_5:
            count += 5
        elif word[i] in list_8:
            count += 8
        elif word[i] in list_10:
            count += 10
    print(f'Вы набрали очков: {count}')
