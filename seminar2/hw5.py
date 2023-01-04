# Реализуйте алгоритм перемешивания списка.

import random
start_list = [1,2,3,4,5]
print (f'Данная программа перемешивает список {start_list}, можно изменить в самом коде')
end_list = start_list
random.shuffle(end_list)
print (f'Конечный результат {end_list}')