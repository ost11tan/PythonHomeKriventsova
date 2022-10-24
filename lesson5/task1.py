#Напишите программу, удаляющую из текста все слова, содержащие "абв".
# -*- coding: utf-8 -*-

text = open('lesson5task1.txt','r',encoding="utf-8").read()
list=text.split()


#text = " абв авб дтлмлщ липоабвоп дмдрщеоал авб авбгдейка тмтпрпщрл цьурсызцд  абвгденьги оиьепша ьаоущд абв тпопшуьт холджабвщод хзщлотлдждл9542" //реализация не через файл
#list=text.split()


print(list)
found="абв" 


new_list = [] 
for i in range(len(list)) : 
    if found not in list[i]:
        new_list.append(list[i])
print(new_list)


with open('lesson5task1_result.txt', 'w') as data:
    text=str(new_list)
    data.write(text)
data.close()