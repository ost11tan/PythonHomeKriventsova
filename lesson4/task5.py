#5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file.txt', 'r') as data:
    l =[line.strip() for line in data]
data.close()

with open('file2.txt', 'r') as data:
    l1 = [line.strip() for line in data]
data.close()

stroka=str(l[0])
stroka2=str(l1[0])

num=[]
for i in range (2,len(stroka)): #реализация адекватна только,если все коэффициенты двухзначные
    if stroka[i]=="X":
        temp=stroka[i-2]+stroka[i-1]
        num.append(temp)
        
#print(list)

list2=[]
for i in range (2,len(stroka2)): #реализация адекватна только,если все коэффициенты двухзначные
    if stroka2[i]=="X":
        temp=stroka2[i-2]+stroka2[i-1]
        list2.append(temp)

#print(list2)

for i in range(len(num)):
    num[i]=int(num[i])+int(list2[i])
list1=list(reversed(num))    
with open('file3.txt', 'w') as data:
    for i in range(len(list1)-1, -1, -1):
        if i==len(list1)-1:
            data.write(str(list1[i])+"X^"+str(i+1))
        else:
            data.write ("+"+str(list1[i])+"X^"+str(i+1))
data.close()