import telebot
token = '5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет,")
                     
                     
if __name__ == '__main__':
     bot.infinity_polling()
