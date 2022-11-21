import print1
import telebot
from telebot import types # для указание типов  
import delete
import edit
import add
import search
token='5931103429:AAEsZN6RJ_QLVkFRAtyupMBUjkJ_F6pa240'
bot=telebot.TeleBot(token)



    
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("База данных сотрудников.")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для лабы№8, давай поработаем с базой данных".format(message.from_user), reply_markup=markup)
    
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
        
    elif message.text == "Добавить запись.":
        add.reading(token) 
        
    elif message.text == "Найти запись.":
        search.Search_Entry('employees.csv')
        bot.send_message(message.chat.id, text="функция для поиска записи ")
    elif message.text == "Изменить запись.":
        edit.Edit_Entry('employees.csv')
        bot.send_message(message.chat.id, text="функция для корректировки записи")
    elif message.text == "Удалить запись.":
        bot.send_message(message.chat.id, text="Введите элемент имя сотрудника для удаления данных о нём из БД")
        delete.delete_str('employees.csv', get_text_messages(message))
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("База данных сотрудников.")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован")
def get_text_messages(message):
    return message.text
bot.polling(none_stop=True)