personInfo = {'Крис эванс':'Мстители, Одоренная',
              'Роберт Дауни Младщий':'Мстители Шерлок холмс',
              'марк руффало':'Остров проклятых,Хоть раз в жизни'}


name = input('Введите актера')
name = name.lower()

if name in personInfo:
    print(personInfo[name])
else:
    print('Такого актера нет')
