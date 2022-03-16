import telebot
token = '5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['t'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.
first_name}!".format(message.from_user))
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
     bot.infinity_polling()
