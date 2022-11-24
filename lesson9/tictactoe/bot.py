import telebot
from telebot import types # для указание типов  
import list_to_stroka
import test
import random
token='5915737731:AAFdzztSK2naeQyhfTvmKm_3MLiDjza-9DA'
bot=telebot.TeleBot(token)


mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
global count
row=0
elem=0

def  PRINT(message,mass) :
    row1=list_to_stroka.lst_to_str(mass,0)
    row2=list_to_stroka.lst_to_str(mass,1)
    row3=list_to_stroka.lst_to_str(mass,2)
    st=row1+"\n"+row2+"\n"+row3
    bot.send_message(message.chat.id,text=st)



@bot.message_handler(commands=["start"])
def game(message): 
    bot.send_message(message.chat.id, "Пришли любое сообщение,чтобы начать ")


@bot.message_handler(content_types=["text"])
def inputs(message,res=False):
    bot.send_message(message.chat.id, "Вы ходите первым!")
    PRINT(message,mass)  
    count=0
    for count in range (9):
        count=count+1
        if count%2==0:
            imputForX(message)
            PRINT(message,mass)
            test.WinX(mass) 
        else:
            imputForO(message,mass)
            PRINT(message,mass)
            test.WinO(mass)
    
        if count==9:
            bot.send_message(message.chat.id,"Игра окончена. Результ- ничья")
    
def ForX(message):
    imputForX(message)    
    
    
def  imputForX(message,res=True):
    bot.send_message(message.from_user.id, "☑️ Введите номер строки")
    bot.register_next_step_handler(message, get_rowX)
def get_rowX(message):
    row=int(message.text)-1
    if row>=0 and row<=2:
        bot.send_message(message.from_user.id, "☑️ Введите номер стoлбца")
        bot.register_next_step_handler(message,get_colomnX)
        
    else:
        bot.send_message(message.chat.id,"Вы вышли за пределы поля,попробуйте еще раз")
        bot.register_next_step_handler(message, imputForX)
    
         
def get_colomnX(message):
    elem=int(message.text)-1
    if elem<0 and elem>2:
        bot.send_message(message.chat.id,"Вы вышли за пределы поля,попробуйте еще раз ввеcти номер столбца")
        get_colomnX(message) 
    else:
        PrintX(message,mass)
        
        
def PrintX(message,mass):  
    if mass[row][elem]=="🔲":
        mass[row][elem] = "☑️"  
    else:
        bot.send_message(message.chat.id,"Этот элемент уже занят игроком " + str (mass[row][elem])+" введите координаты другого свободного места")
        imputForX(message)      

def imputForO(message,mass):
    row=random.randint(0, 2)
    elem=random.randint(0, 2)
    if mass[row][elem]=="🔲":
        mass[row][elem] = "🔘" 
    else:
        imputForO(message,mass)



                   


bot.polling(none_stop=True, interval=0)