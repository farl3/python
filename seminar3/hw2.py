# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def generate_random_list(min_value=0, max_value=9, length_list=5):
    random_list = []
    for _ in range(length_list):
        random_list.append(random.randint(min_value, max_value))
    return random_list

def custom_list(random_list):
    result_list = []
    flag = True
    i = 0
    list_end = len(random_list) - 1
    while flag:
        result_list.append(random_list[i]*random_list[list_end-i])
        if (i == list_end - i) or (i + 1 == list_end - i):
            flag = False
        i += 1
    return result_list

random_length = random.randint(4, 7)
any_list = generate_random_list(0, 9, random_length)
print (any_list, end=' ')
result_list = custom_list(any_list)
print(f'-> {result_list}')