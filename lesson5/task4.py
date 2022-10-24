#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

#Пример
#	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

#Проблема с 17Е,не получается сообразить как выходить за десяток....он читает 1,потом перезаписывает счетик на 7 (есть идея сначала 7,потом 10 раз напечатать,соответственно сотню,если 3 цифры подряд)


with open('less5task4sours.txt', 'r') as data:
    l =[line.strip() for line in data]
data.close()
text=str(l[0])
print(text)

count = 1
New = ''
for i in range(len(text)-1):
    if text[i] == text[i+1] and i!=len(text)-2:
        count=count+1
    elif i==len(text)-2:
        count=count+1
        New = New + str(count) + text[i]  
    else:
        New = New + str(count) + text[i]
        count = 1
    
        
    

print(New)
with open('less5task4code.txt', 'w') as data:
    data.write(New)
data.close()


#декодировка
with open('less5task4code.txt', 'r') as data:
    l =[line.strip() for line in data]
data.close()
text=str(l[0])
print(text)

New2 = ''
for i in range (len(text)):
    if text[i].isdigit():
        count=int(text[i])
    else:
        for j in range (count):
            New2=New2+text[i]
print(New2)
with open('less5task4decode.txt', 'w') as data:
    data.write(New2)
data.close()