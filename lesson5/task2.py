#2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

 #b) Подумайте как наделить бота "интеллектом"
 
def candy (table,play):
    print("Ход игрока " + str (play))
    cand=int(input("Введите количество конфет "))
    if cand<1 or cand>28:
        print("Введите корректное количество конфет")
        candy(table,play)
    else:
        table=table-cand
        print("На столе осталось "+ str(table)+" ход следующего игрока")  
        #return table
    return table 
    
    
count=2021 #Изначальное количество конфет
i=0
while count>0:
    i+=1
    if i%2==0:
        player=1
        count=candy(count,player)
    else:
        player=2
        count=candy(count,player)
if count<=0:
    print("Победил игрок "+str(player))
