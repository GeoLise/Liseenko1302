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
    markup.add(item1)
    bot.send_message(message.chat.id,'Ну да', reply_markup=markup)
    item2=types.KeyboardButton
    markup.add(item1)
    bot.send_message(message.chat.id,'Ага', reply_markup=markup)

if __name__ == '__main__':
     bot.infinity_polling()
