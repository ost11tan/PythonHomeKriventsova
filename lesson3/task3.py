#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


n = int(input("Введите число N "))
summ=0
if n<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    list = []
    for i in range(n) : 
        list.append(random.uniform(0, 50))
    print(list)
    
    for i in range (n):
        list[i]=list[i]%1
        
    min=list[0]
    max=list[0]

    for i in range(n):
        if list[i]>0:
            temp=list[i]
            min_number = lambda min, temp: min if min < temp else temp
            min=min_number(min,temp)
        if list[i]>max:
            max=list[i]
    print("Разница между максимальным и минимальным значениеми дробных частей " + str(round((max-min),2)))
 
            
        