# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def generate_fibonacci(k):
    result_list = []
    for i in range(0, k + 1):
        if i == 0:
            result_list.append(int(0))
        elif i < 3:
            result_list.append(int(1))
        else:
            result_list.append(result_list[i-1] + result_list[i-2])
    return result_list

def generate_negafibonacci(fibonacci_list):
    result_list = []
    for i in range(len(fibonacci_list) - 1, 0, -1):
        power_fib = (-1) ** (i+1)
        result_list.append(power_fib * fibonacci_list[i])
    return result_list


num = int(input('Введите целое число k: '))
fibonacci_list = generate_fibonacci(num)
negafibonacci_list = generate_negafibonacci(fibonacci_list)
print (negafibonacci_list + fibonacci_list)