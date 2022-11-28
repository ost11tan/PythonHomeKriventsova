import telebot
from telebot import types # для указание типов  
import Sum
import sub
import div
import model_mult
import logger
import print1
token='5659797931:AAFZJ1_49peLhVmkqZJEAxkna8BSlDvqEpo'
bot=telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начало")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот-калькулятор. Нажми <<Начало>>".format(message.from_user), reply_markup=markup)
    
def get_a(message):
    global a
    a=float(message.text)   
    bot.send_message(message.chat.id,"Введите b")
    bot.register_next_step_handler(message, get_b) 
def get_b(message):
    global b
    b=float(message.text)
    bot.send_message(message.chat.id,"Что вы хотите сделать с этими числами?")
    
def get_ai(message):
    global ai
    ai=complex(message.text)
    bot.send_message(message.chat.id,"Введите b")
    bot.register_next_step_handler(message, get_bi) 
def get_bi(message):
    global bi
    bi=complex(message.text)
    bot.send_message(message.chat.id,"Что вы хотите сделать с этими числами?")
    
@bot.message_handler(content_types=['text'])  
def func(message):
    if(message.text == "Начало"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
        btn1 = types.KeyboardButton("Рациональные числа")
        btn2 = types.KeyboardButton("Комплексные числа")
        btn3 = types.KeyboardButton("Посмотреть log")
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        
    elif(message.text == "Рациональные числа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)   
        btn1 = types.KeyboardButton("Ввести два числа")
        btn2 = types.KeyboardButton("➕")
        btn3 = types.KeyboardButton("➖")
        btn4 = types.KeyboardButton("✖️")
        btn5 = types.KeyboardButton("➗")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3, btn4,btn5, back)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        
    
    elif(message.text == "Ввести два числа"):
        bot.send_message(message.chat.id,"Введите а")
        bot.register_next_step_handler(message, get_a)
        
    elif(message.text == "➕"):
        res=Sum.Sum(a,b)
        bot.send_message(message.chat.id, text=res)
        logger.sum_logger(a,b,res)
    elif(message.text == "➖"):
        res=sub.do_it(a,b)
        bot.send_message(message.chat.id, text=res)
        logger.sub_logger(a,b,res)
    elif(message.text == "✖️"):
        res=model_mult.do_it(a,b)
        bot.send_message(message.chat.id, text=res)
        logger.mult_logger(a,b,res)
    elif(message.text == "➗"):
        res=div.Div(a,b)
        bot.send_message(message.chat.id, text=res)
        logger.div_logger(a,b,res)
        
    elif(message.text == "Комплексные числа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)   
        btn1 = types.KeyboardButton("Ввести два числа(i)")
        btn2 = types.KeyboardButton("➕i")
        btn3 = types.KeyboardButton("➖i")
        btn4 = types.KeyboardButton("✖️i")
        btn5 = types.KeyboardButton("➗i")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3, btn4,btn5, back)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        
    
    elif(message.text == "Ввести два числа(i)"):
        bot.send_message(message.chat.id,"❗️ВНИМАНИЕ❗️\nКомплексные числа вводятся в формате <<a+bj>>\nэто значит ,что просто 10 будет выглядеть как 10+0j,\nа 12j как 0+12j")
        bot.send_message(message.chat.id,"Введите а")
        bot.register_next_step_handler(message, get_ai)
        
    elif(message.text == "➕i"):
        res=Sum.Sum(ai,bi)
        bot.send_message(message.chat.id, text=res)
        logger.sum_logger(ai,bi,res)
    elif(message.text == "➖i"):
        res=sub.do_it(ai,bi)
        bot.send_message(message.chat.id, text=res)
        logger.sub_logger(ai,bi,res)
    elif(message.text == "✖️i"):
        res=model_mult.do_it(ai,bi)
        bot.send_message(message.chat.id, text=res)
        logger.mult_logger(ai,bi,res)
    elif(message.text == "➗i"):
        res=div.Div(ai,bi)
        bot.send_message(message.chat.id, text=res)
        logger.div_logger(ai,bi,res)
        
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начало")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        
    elif(message.text == "Посмотреть log"):
        txt=print1.print_all_to_console()
        bot.send_message(message.chat.id, text=txt)


bot.polling(none_stop=True, interval=0)