#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from functools import reduce
import random
#import datetime
#b1=10
#b2=20

n = int(input("Введите число N "))
summ=0
if n<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    list = []
    for i in range(n) : 
        #a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
        #a=a%1
        #a=round(b1+(b2-b1)*a)
        #list.append(a)
        list.append(random.randint(0, 50))   #Закоментирована попытка вставить код из семинара,выдает массив одинаковых рандомных значений
    print(list)
    
    summ=0
    new_list=[]
    for i in range(n):
        if i%2==1:
            new_list.append(list[i])
            
    print("На нечетных позициях находятся числа :"+str(new_list))        
    summa = reduce((lambda x, y: x + y), new_list)
    
    print("Ответ:"+str(summa))