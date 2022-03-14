import telebot
token = '5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY'
bot = telebot.TeleBot(5163401707:AAHqHabhzFXDz2gMFlrDZVabNEgHrO1UswY)
@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)

if_name_=='_main_':
    bot.infinity_polling()
