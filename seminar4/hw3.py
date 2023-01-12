# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def generate_random_list(min_value=0, max_value=5, length_list=10):
    random_list = []
    for _ in range(length_list):
        random_list.append(random.randint(min_value, max_value))
    return random_list

def find_unique_values(random_list):
    result_list = []
    for i in random_list:
        if random_list.count(i) == 1:
            result_list.append(i)
    return result_list

any_list = generate_random_list()
unique_values = find_unique_values(any_list)
if not unique_values:
    print(f'В списке {any_list} нет неповторяющихся элементов')
else:
    print(f'В списке {any_list} значения {unique_values} не повторяются')