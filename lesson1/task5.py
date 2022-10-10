#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21

import math
x1 = float(input("Введите координаты точки А \nX= "))
y1 = float(input("Y= "))
x2 = float(input("Введите координаты точки B \nX= "))
y2 = float(input("Y= "))


distanceSqr= (x2-x1)**2+(y2-y1)**2
distance=math.sqrt(distanceSqr)

print("Расстояние между точкими А и В = " + str(distance))