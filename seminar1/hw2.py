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



# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

# print('x','y','z', 'w' )
# for x in range (2):
#     for y in range (2):
#         for z in range (2):
#             for w in range (2):
#                 if not ((w and z) or not y or (not x == (not w))):
#                     print(x, y, z, w)
