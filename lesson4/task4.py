#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Задайте натуральную степень k "))

if k<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    degree = []
    for i in range(k) : 
        degree.append(random.randint(0, 100)) 
    print(degree)
    
    #f = open('text.txt', 'w')
    with open('file.txt', 'w') as data:
        for i in range(k-1, -1, -1):
            if i==k-1:
                data.write(str(degree[i])+"X^"+str(i+1))
            else:
                data.write ("+"+str(degree[i])+"X^"+str(i+1))
    data.close()
