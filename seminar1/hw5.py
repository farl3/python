#Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

from math import sqrt

x_a = int(float(input("Введите x_a: ")))
x_b = int(float(input("Введите x_b: ")))
y_a = int(float(input("Введите y_a: ")))
y_b = int(float(input("Введите y_b: ")))

dist = round(sqrt((x_b - x_a)**2 + (y_b - y_a)**2), 2)
print(f"Расстояние между A: {(x_a, y_a)} и B {(x_b, y_b)} равно {dist}")