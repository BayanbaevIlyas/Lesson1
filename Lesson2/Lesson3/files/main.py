my_file = open('testfile.vik','a',encoding='utf-8')

last_name = input('Введите Фамилию: ')
firs_name = input('Введите имя: ')
middle_name = input('Введите отчество: ')
fio = last_name + '' + first_name + '' + middle_name + '\n'
my_file.write(fio)
my_file.close()
