#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

import random


n = int(input("Введите число N "))
summ=0
if n<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    list = []
    for i in range(n) : 
        list.append(random.randint(0, 50))
    print(list)
    
    list2=[]
    for i in range (n):
        if i<n/2 and i!=(n-i-1):
            temp = list[i]*list[n-i-1]
            list2.append(temp)
    print (list2)