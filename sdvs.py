import telebot
from telebot import types
token = '5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!".format(message.from_user))
                     
@bot.message_handler(commands=["button"])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    item2=types.KeyboardButton("Кнопка2")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Ну да', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_photo(message.chat.id, photo=open('vze2.jpg', 'rb'))
        
if __name__ == '__main__':
     bot.infinity_polling()
