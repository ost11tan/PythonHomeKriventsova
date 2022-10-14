#5. Реализуйте алгоритм перемешивания списка.



import random


n=10

list = []
for i in range (n):
    list.append(random.randint(0, 50))
print(list)

random.shuffle(list)  #реализация через функцию
print (list)


for i in range (n):
    if i<n/2:
        temp=list[i]
        list[i]=list[n-i-1]
        list[n-i-1]=temp
print(list)