# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def parse_equation(equation_string):
    equation_string = equation_string.replace('-','+-')
    equation_string = equation_string.lstrip('+')
    equation_string = equation_string.replace(' ','')
    equation_string = equation_string.split('=')[0]
    equation_string = equation_string.split('+')
    last_power = 0
    params_list = []
    for i in equation_string:
        temp = i.split('*')
        if len(temp) > 1:
            temp_power = int(temp[1].split('^')[1])
            if last_power > 0:
                while last_power - temp_power > 1:
                    params_list.append(0)
                    last_power -= 1
            else:
                last_power = temp_power
        if last_power == 2 and len(params_list) == 1:
            params_list.append(0)
        params_list.append(int(temp[0]))
    return params_list

def get_new_params(equation_string_1, equation_string_2):
    first_params = parse_equation(equation_string_1)
    second_params = parse_equation(equation_string_2)
    if len(first_params) < len(second_params):
        first_params, second_params = second_params, first_params
    shift = len(first_params) - len(second_params)
    for i in range (0, len(second_params)):
        first_params[i+shift] += second_params[i]
    return first_params

def generate_equation(params_list):
    equation_power = len(params_list)
    result = ''
    for i in params_list:
        equation_power -= 1
        if i != 0:
            result += f'{i}'
            if equation_power > 0:
                result += f'*x^{equation_power} + '
    result += ' = 0'
    return result

file_obj_1 = open('hw5_1.txt', 'r')
file_obj_2 = open('hw5_2.txt', 'r')
equation_string_1 = file_obj_1.readline()
equation_string_2 = file_obj_2.readline()
file_obj_1.close()
file_obj_2.close()
print(f'Формула многочлена из первого файла: {equation_string_1}')
print(f'Формула многочлена из второго файла: {equation_string_2}')
params_list = get_new_params(equation_string_1, equation_string_2)
new_equation_string = generate_equation(params_list)
print(f'Формула результирующего многочлена: {new_equation_string}')
file_obj = open('hw5.txt', 'w')
file_obj.write(new_equation_string)
file_obj.close()