#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# #Негафибоначчи
# Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k= int(input("Введите число k "))


fibonachi=[]

if k>=0:
    for i in range(k):
        if i<2:
            start=1
            fibonachi.append(start)
        if i>=2:
            fib_sum=fibonachi[i-1]+fibonachi[i-2]
            fibonachi.append(fib_sum)
            
    
    Negative=[]
    for i in range(k):
        temp=fibonachi[k-i-1]
        Negative.append(temp)
    i=k-2
    while i>=0:
        Negative[i]=-Negative[i]
        i=i-2
        
            
    Negative.append(0)
    Negative.extend(fibonachi)
    
    print(Negative)
