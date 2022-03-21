import telebot
from telebot import types
token = '5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    item2=types.KeyboardButton("Кнопка2")
    markp.add(item1, item2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_photo(message.chat.id, photo=open('vze2.jpg', 'rb'))
    if message.text=="Кнопка2":
        bot.send_message(message.chat.id, "vk.com/goshkazavr")
if __name__ == '__main__':
     bot.infinity_polling()

        bot.send_message(message.chat.id,text="Привет, {0.first_name}!".format(message.from_user))
