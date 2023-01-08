# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

def generate_random_list(min_value=0.0, max_value=9.9, length_list=5, length_round=2):
    random_list = []
    for _ in range(length_list):
        random_list.append(round(random.uniform(min_value, max_value), length_round))
    return random_list

def custom_rule(random_list):
    min_value = 0.99
    max_value = 0.0
    for i in range(len(random_list)):
        temp = random_list[i] % 1
        if temp < min_value:
            min_value = temp
        if temp > max_value:
            max_value = temp
    return round(max_value - min_value, 2)

any_list = generate_random_list()
print (any_list, end=' ')
difference_in_list = custom_rule(any_list)
print(f'-> {difference_in_list}')