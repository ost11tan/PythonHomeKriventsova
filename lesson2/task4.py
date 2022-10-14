#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.




import random


n = int(input("Введите число N "))

if n<1:
    print ("Данное значение не удовлетворяет условию задачи,введите число больше или равное 1")
else:
    list = []
    for i in range (n):
        list.append(random.randint(-n, n))
    print(list)

    summ=1
    

    #f = open('D:\учеба\PythonHomeKriventsova\lesson2\file.txt', 'r')   переименовала файл тк ругался на \f
    f = open('D:\учеба\PythonHomeKriventsova\lesson2\File.txt', 'r') 
    l = [line.strip() for line in f]
    f.close()
    
    for i in range (len(l)):
        k=int(l[i])
        summ=summ*list[k]
    print(summ)
    

