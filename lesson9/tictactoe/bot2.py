import telebot
from telebot import types # для указание типов  
import list_to_stroka
import test
import random
token='5915737731:AAFdzztSK2naeQyhfTvmKm_3MLiDjza-9DA'
bot=telebot.TeleBot(token)


mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
global count
count=0
row=0
elem=0

def  PRINT(message,mass) :
    row1=list_to_stroka.lst_to_str(mass,0)
    row2=list_to_stroka.lst_to_str(mass,1)
    row3=list_to_stroka.lst_to_str(mass,2)
    st=row1+"\n"+row2+"\n"+row3
    bot.send_message(message.chat.id,text=st)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Ты ходишь первый!".format(message.from_user), reply_markup=markup)
     
def Test_X(message,mass):
    global count
    count=count+1
    if test.WinX(mass)==True:
        bot.send_message(message.chat.id,"Выиграл ☑️")
        mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
        
    elif count>=8:
        bot.send_message(message.chat.id,"Игра окончена с результатом <<Ничья>>")
        mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
    return mass    
               
         
    
def imputForO(message,mass):
    global count
    row=random.randint(0, 2)
    elem=random.randint(0, 2)
    if mass[row][elem]=="🔲":
        mass[row][elem] = "🔘" 
        PRINT(message,mass) 
        count=count+1
        if test.WinO(mass)==True:
            bot.send_message(message.chat.id,"Выиграл 🔘")
            mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
            
        elif count>=8:
            bot.send_message(message.chat.id,"Игра окончена с результатом <<Ничья>>")
            mass = [["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"], ["🔲", "🔲", "🔲"]]
    
    else:
        imputForO(message,mass)  
    return mass    
            
        
       
@bot.message_handler(content_types=['text'])  
def func(message):
    if(message.text == "Начать игру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
        btn1 = types.KeyboardButton("☑️1")
        btn2 = types.KeyboardButton("☑️2")
        btn3 = types.KeyboardButton("☑️3")
        btn4 = types.KeyboardButton("☑️4")
        btn5 = types.KeyboardButton("☑️5")
        btn6 = types.KeyboardButton("☑️6")
        btn7 = types.KeyboardButton("☑️7")
        btn8 = types.KeyboardButton("☑️8")
        btn9 = types.KeyboardButton("☑️9")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3, btn4,btn5,btn6,btn7,btn8,btn9, back)
        bot.send_message(message.chat.id, text="Какую ячейку вы хотите занять?", reply_markup=markup)
    
    elif(message.text == "☑️1" ):
        if mass[0][0] == "🔲" :
            mass[0][0] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
        
    elif(message.text == "☑️2" ):
        if mass[0][1] == "🔲" :
            mass[0][1] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
        
    elif(message.text == "☑️3" ):
        if mass[0][2] == "🔲" :
            mass[0][2] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️4" ):
        if mass[1][0] == "🔲" :
            mass[1][0] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️5" ):
        if mass[1][1] == "🔲" :
            mass[1][1] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️6" ):
        if mass[1][2] == "🔲" :
            mass[1][2] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️7" ):
        if mass[2][0] == "🔲" :
            mass[2][0] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️8" ):
        if mass[2][1] == "🔲" :
            mass[2][1] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif(message.text == "☑️9" ):
        if mass[2][2] == "🔲" :
            mass[2][2] = "☑️" 
            Test_X(message,mass)
            PRINT(message,mass) 
            imputForO(message,mass)
        else:bot.send_message(message.chat.id,"Выберите свободную ячейку")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать игру")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        
      
    
    
    
bot.polling(none_stop=True, interval=0)