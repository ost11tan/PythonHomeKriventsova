#Вычислить число c заданной точностью d
#Пример:
#при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10


d = int(input("Введите количество знаков после запятой "))
list = []

num=4/1 
list.append(num)
num=num - 4/3 + 4/5
list.append(num)
k=7
i=1

while ((round(list[i-1],d) != round(list[i],d))):
    i=i+1
    
    numer=lambda num,k :num - 4/k + 4/(k+2)
    list.append(numer(num,k))
    num=numer(num,k)
    k=k+4
    
#print (list)
p=round(list[len(list)-1],d)
print ("Число П = " + str(p))

