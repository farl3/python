# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_simple_numbers(num):
    temp_list = list(range(2, num + 1))
    for i in temp_list:
        j = 2
        while i * j <= num:
            if i * j in temp_list:
                temp_list.remove(i * j)
            j += 1
    return temp_list

def get_simple_multipliers(num):
    simple_list = get_simple_numbers(num)
    result_list = []
    for i in simple_list:
        if num % i == 0:
            result_list.append(i)
    return result_list

num = int(input('Введите натуральное число N: '))
multipliers_list = get_simple_multipliers(num)
if not multipliers_list:
    print(f'У числа {num} нет простых делителей')
else:
    print(f'Для числа {num} числа {multipliers_list} являются простыми делителями')