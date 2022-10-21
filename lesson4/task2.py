#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input("Введите число N "))

if n<0:
    print("Число не является натуральным")
else:
    list=[]
    for i in range (n):
        if i>0:
            num=n%i
            if num==0:
                list.append(i)
                n=n/i  
                
    if len(list)==1:
        list.append(int(n))
    #print (list)
    
    if len(list)>2:
        list2=[]
        list2.append(list[0])
        list2.append(list[1])
        flag=0
        for i in range(len(list)):
            if i>1:
                for j in range(list[i]-1):
                    if j>1:
                        if list[i]%j == 0:
                            flag=1    
                if flag==0:
                    list2.append(list[i])
            flag=0
        print (list2)
    else:
        print (list)
    