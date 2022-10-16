
#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#45 -> 101101
#3 -> 11
#2 -> 10


n = int(input("Введите число N "))

num=[]
temp=n

if n>=0:
    for i in range(n):
        while temp>0:
            num.append(temp%2)
            temp=int(temp/2)
    list1=list(reversed(num))
    print (list1)
else:
    print("В задаче не требовалось реализовать перевод отрицательных чисел")
    #num=-num
    #for i in range(n):
    #    while temp>0:
    #        num.append(temp%2)
    #        temp=int(temp/2)
    #list1=list(reversed(num))
    #for i in range(n):
    #    if list1[i]==1:
    #        list[i]=0
    #    else:
    #        list[i]=1
    
    #Далее побитовое сложение с 1 ,вот тут не совсем понимаю как реализовать,но,если правильно понял задание отрицательные и не нужно было