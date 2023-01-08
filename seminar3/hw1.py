# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

def generate_random_list(min_value=0, max_value=9, length_list=5):
    random_list = []
    for _ in range(length_list):
        random_list.append(random.randint(min_value, max_value))
    return random_list

def custom_sum(random_list):
    result = 0
    result_list = []
    for i in range(1, len(random_list), 2):
        result += random_list[i]
        result_list.append(random_list[i])
    return (result, result_list)

any_list = generate_random_list()
print (any_list, end=' ')
(sum_in_any_list, elements) = custom_sum(any_list)
print(f'-> на нечетных позициях элементы {elements}, ответ: {sum_in_any_list}')