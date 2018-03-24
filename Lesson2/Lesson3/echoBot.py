import telebot
token = '462539917:AAFdizUx-8GpepdUfNfhwKsv4g3d4n2j3M4'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types = ['text'])
def check_message(message):
    if message.text == 'Скажи да':

        bot.send_message(message.chat.id, 'нет')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)

