import telebot
token = '462539917:AAFdizUx-8GpepdUfNfhwKsv4g3d4n2j3M4'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types = ['text'])
def check_message(message):
    bot.send_message(message.chat.id, message.text)
    name = input('Введите слово')
    name[-1]
    name = message



bot.polling(none_stop=True)

