import print1
import telebot
from telebot import types # для указание типов  
import delete
import edit
import add
import search
import list_to_stroka_sy
token='5931103429:AAEsZN6RJ_QLVkFRAtyupMBUjkJ_F6pa240'
bot=telebot.TeleBot(token)


   
contacts=[None]*5 
def get_num(message): 
    contacts[0]= message.text
    bot.send_message(message.from_user.id, "Введите фамилию:")
    bot.register_next_step_handler(message, get_surname);   
def get_surname(message): 
    contacts[1]= message.text
    bot.send_message(message.from_user.id, "Введите имя:")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    contacts[2]= message.text
    bot.send_message(message.from_user.id, "Введите Телефон: ")
    bot.register_next_step_handler(message, get_number)
        
def get_number(message):
    contacts[3]= message.text
    bot.send_message(message.from_user.id, "Введите описание: ")
    bot.register_next_step_handler(message, get_comment)
    
def get_comment(message):
    contacts[4]= message.text
    print(contacts)
    add.newstring(contacts)    
    
    
    
    
      
def get_del(message):
    num=message.text
    delete.delete_str("employees.csv",num)
def get_search(message):
    num=message.text
    txt=search.Search_Entry('employees.csv',num)
    bot.send_message(message.chat.id, text=txt)
    
    
    
def get_edit(message):
    num=message.text
    global old
    old=search.Search_Entry('employees.csv',num)
    #old=list_to_stroka_sy.lst_to_str(old)
    bot.send_message(message.chat.id, text=old)
    bot.send_message(message.chat.id, text="На что заменить,введите номер записи:")
    bot.register_next_step_handler(message, get_num1)
    

def get_num1(message): 
    contacts[0]= message.text
    bot.send_message(message.from_user.id, "Введите фамилию:")
    bot.register_next_step_handler(message, get_surnam1);   
def get_surnam1(message): 
    contacts[1]= message.text
    bot.send_message(message.from_user.id, "Введите имя:")
    bot.register_next_step_handler(message, get_nam1)

def get_nam1(message):
    contacts[2]= message.text
    bot.send_message(message.from_user.id, "Введите Телефон: ")
    bot.register_next_step_handler(message, get_number1)
        
def get_number1(message):
    contacts[3]= message.text
    bot.send_message(message.from_user.id, "Введите описание: ")
    bot.register_next_step_handler(message, get_comment1)
    
def get_comment1(message):
    contacts[4]= message.text
    print(contacts)
    edit.Edit_Entry(old,contacts)



   
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
        bot.send_message(message.from_user.id, "Введите номер записи:")
        bot.register_next_step_handler(message, get_num)
        
        
        
    elif message.text == "Найти запись.":
        bot.send_message(message.chat.id, text="Введите элемент имя сотрудника для поиска в БД:")
        bot.register_next_step_handler(message, get_search)
        
    elif message.text == "Изменить запись.":
        bot.send_message(message.chat.id, text="Введите элемент - номер сотрудника  в БД:")
        bot.register_next_step_handler(message, get_edit)
        
        
    elif message.text == "Удалить запись.":
        bot.send_message(message.chat.id, text="Введите номер элемента для удаления данных о нём из БД")
        bot.register_next_step_handler(message, get_del)
        
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("База данных сотрудников.")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован")


bot.polling(none_stop=True)






