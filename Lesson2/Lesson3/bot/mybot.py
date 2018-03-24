#Это бот, который работает со списком учениковфывыфв
import telebot
import list3
token = '462539917:AAFdizUx-8GpepdUfNfhwKsv4g3d4n2j3M4'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types = ['text'])
def check_message(message):
        if message.text == 'список студентов':
                for student in list3.get_List_Students():
                        bot.send_message(message.chat.id, 'Имя' + student[0])
                        
        elif message.text == 'Сред. оценка':
                 bot.send_message(message.chat.id, list3.getAverStudMark())
        elif message.text.isdigit():
                 bot.send_message(message.chat.id,
                                 'Имя' + str(list3.getStudentByIndex(int(message.text))[0]))
                 bot.send_message(message.chat.id,
                                 'Оценка' + str(list3.getStudentByIndex(int(message.text))[1]))

                     
        else:
                 bot.send_message(message.chat.id, 'Такой команды я незнаю')
                 
bot.polling(none_stop=True)
