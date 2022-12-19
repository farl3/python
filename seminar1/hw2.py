# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#  для всех значений предикат.

print('Программа для проверки истинности утверждения')
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end=' ')
print('для всех значений предикат.')
print()
print('X','Y','Z' )
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(x, y, z)
            p1 = not (x or y or z)
            p2 = not x and not y and not z
            print(p1 == p2)