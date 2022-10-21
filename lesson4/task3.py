#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input("Введите количество элементов списка "))
if n<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    num = []
    for i in range(n) : 
        num.append(random.randint(0, 10)) 
    print(num)
    
    
    #list2=list(set(num))   решение задачи через функцию set
    #print (list2)
    
    num_uniq = []
    for i in range(n) : 
        if num[i] not in num_uniq:
            num_uniq.append(num[i])
    print(num_uniq)