# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print('Данная программа принимает на вход натуральное число N, создаем список [-N, N] и находит произведение элементов согласно инструкциям в файле.')
num = input('Введите натуральное число N: ')
if num.isdigit():
    num = int(num)
    res_list =  list(range(-num, num+1))
    print(f'Список для числа {num} равен {res_list}')
    multiply = 1
    multiply_list = []
    file_obj = open("file.txt")
    file_lines = file_obj.readlines()
    for line in file_lines:
        line = line.rstrip('\n')
        if line.isdigit():
            temp = int(line)
            multiply_list.append(temp)
            if temp < len(res_list):
                multiply *= res_list[temp-1]
    file_obj.close()
    print(f'Произведение элементов списка под номерами {multiply_list} равно {multiply}, где 1 соответствует нулевому элементу')
else:
    print('Введена строка, попробуйте снова')