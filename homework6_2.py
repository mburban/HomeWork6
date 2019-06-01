# Написать программу для поиска разницы между максимальным и минимальным числом среди num_limit случайно
# сгенерированных чисел в указанном числовом диапазоне.

# import random
#
# # создание диапазона со случайным начальным и конечным значением
# int_range = range(random.randint(0, 10), random.randint(11, 20))
# print(int_range)
#
# # объявление переменной с наименьшим числом в диапазоне
# min_number = int_range[0]
#
# # объявление переменной для наибольшего числа в диапазоне
# max_number = 0
#
# # поиск наибольшего числа в диапазоне
# for i in int_range:
#     if i > 0:
#         i += 1
#         max_number = i
#
# # поиск разницы между наибольшим и наименьшим числом в диапазоне
# difference = max_number - min_number
#
# # вывод разницы
# print('Разница между максимальным и минимальным числом диапазона равна {0}'.format(difference))

import random

range_begin = int(input('Введите начало числового диапазона: '))
range_end = int(input('Введите конец числового диапазона: '))
if range_begin <= 0 and range_end <= range_begin:
    print('Начало числового диапазона должно быть больше 0 и меньше конца числового диапазона.')
else:
    number_of_generations = int(input('Укажите сколько раз нужно сгенерировать число: '))
    i = 0
    list_numbers = list()
    while i < number_of_generations:
        random_number = random.randint(range_begin, range_end)
        list_numbers.append(random_number)
        i += 1

    min_number = list_numbers[0]
    max_number = list_numbers[0]
    for x in list_numbers:
        if x > max_number:
            max_number = x
        if x < min_number:
            min_number = x
    difference = max_number - min_number
    print('Сгенирированы числа {0}. Среди них наименьшим является {1}, а наибольшим {2}. Их разница равна {3}.'.format
          (list_numbers, min_number, max_number, difference))
