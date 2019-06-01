# Написать программу для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit
# случайно сгенерированных чисел в указанном числовом диапазоне. Т.е. от суммы четных чисел вычесть
# сумму нечетных чисел.

# import random
#
# # создание диапазона со случайным начальным и конечным значением
# int_range = range(random.randint(1, 10), random.randint(11, 20))
#
# # объявление переменной для суммирования четных значений
# sum_even = 0
#
# # объявление переменной для суммирования нечетных значений
# sum_uneven = 0
#
# # поиск сумм всех четных и всех нечетных значений
# for i in int_range:
#     # суммирование четных значений
#     if i % 2 == 0:
#         sum_even += i
#     # суммирование нечетных значений
#     else:
#         sum_uneven += i
#
# # вывод разницы сумм всех четных и нечетных значений
# print(sum_even - sum_uneven)

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
    sum_even = 0
    sum_uneven = 0
    for i in list_numbers:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_uneven += i

    difference = sum_even - sum_uneven
    print('Сгенирированы числа {0}. Сумма всех четных чисел равна {1}, а сумма всех нечетных равна {2}. '
          'Их разница равна {3}.'.format(list_numbers, sum_even, sum_uneven, difference))
