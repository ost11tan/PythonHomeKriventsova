import telebot
from telebot import types 

def reading(token):
    bot=telebot.TeleBot(token)
    contacts=[""]*4
    @bot.message_handler(content_types=['text'])
    def start(message):
        if message.text == '/reg':
            bot.send_message(message.from_user.id, "Введите фамилию:")
            bot.register_next_step_handler(message, get_surname); 
        else:
            bot.send_message(message.from_user.id, 'Напиши /reg')

    def get_surname(message): 
        contacts[0]= message.text
        bot.send_message(message.from_user.id, "Введите имя:")
        bot.register_next_step_handler(message, get_name)

    def get_name(message):
        contacts[1]= message.text
        bot.send_message(message.from_user.id, "Введите Телефон: ")
        bot.register_next_step_handler(message, get_number)
        
    def get_number(message):
        contacts[2]= message.text
        bot.send_message(message.from_user.id, "Введите описание: ")
        bot.register_next_step_handler(message, get_comment)
    
    def get_comment(message):
        contacts[3]= message.text

  #  bot.polling(none_stop=True)
    return contacts
 



def newstring(contacts):
    bazaopen = open("employees.csv", "a", encoding = 'utf-8')
    bazaopen.write(contacts + '\n')
    bazaopen.close()
    
    
    
    
    
    
    
    
    
    
