films = [['Назат в Будущее',1985,'ПРИКЛЮЧЕНИЕ', 9],
         ['Тор: Рагнарек', 2017, 'Фантастика',9],
         ['Матрица', 1998, 'Боевик',10],
         ['Телохранитель киллера', 2017, 'Комедия', 9],
         ['нтерстерла', 2014, 'фантастика', 10]]
number = 0
while number != 5:
    print ('Введите 1 - показать фильмы по названия')
    print ('2 - показать фильмы по жанру')
    print ('3 - добавить фильм')
    print ('4 - удалить фильм')
    print ('5 - Выйти из программы')

    number = int(input())
    if number == 1:
        name = input('Введите показать фильмы:')
        for film in films:
            if film[0] == name:
                print(film)
    elif number == 2:
        name = input('показать фильмы по жанру:')
        for film in films:
            if film[2] == name:
                print(film)
    elif number == 3:
        name = input('добавить фильм:')
        year = int(input('Введите год выхода'))
        genre = input ('Введите жанр')
        rate = int(input('Введите рейтинг'))
        films.append([name, year, genre, rate])
        
        print('фильм добавлен')
    elif number == 4:
        name = input('удалить фильм')
        for film in films:
            if film[0] == name:
                films.remove(film)
        print ('фильм удален')
        print (films)
    elif number == 5:
        print('пока')
    else:
        print('такого числа нет')
        



    
    




