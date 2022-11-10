#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input("Введите число N "))

if n<0:
    print("Число не является натуральным")
else:
    
    list=[i for i in range(1,n) if n%i==0]
                
    if len(list)==1:
        list.append(int(n))

    if len(list)>2:
        list2=[]
        list2.append(list[0])
        list2.append(list[1])
        flag=0
        for i in range(2,len(list)):
            for j in range(2,list[i]-1):
                if list[i]%j == 0:
                    flag=1    
            if flag==0:
                list2.append(list[i])
            flag=0
        print (list2)
    else:
        print (list)
    