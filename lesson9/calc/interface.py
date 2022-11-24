import telebot
from telebot import types # для указание типов  
import div
token='5659797931:AAFZJ1_49peLhVmkqZJEAxkna8BSlDvqEpo'
bot=telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ввести два числа")
    markup.add(btn1)
    
    
@bot.message_handler(content_types=['text'])  
def func(message):
    if(message.text == "База данных сотрудников."):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
        btn1 = types.KeyboardButton("Вывести все записи")
        btn2 = types.KeyboardButton("Добавить запись.")
        btn3 = types.KeyboardButton("Найти запись.")
        btn4 = types.KeyboardButton("Изменить запись.")
        btn5 = types.KeyboardButton("Удалить запись.")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3, btn4,btn5, back)
        bot.send_message(message.chat.id, text="Что мы хотим сделать? \n1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Выход.\n", reply_markup=markup)
    
    elif(message.text == "Вывести все записи"):
        list=print1.print_all_to_console("employees.csv")
        bot.send_message(message.chat.id, text=list)
    
    


bot.polling(none_stop=True, interval=0)