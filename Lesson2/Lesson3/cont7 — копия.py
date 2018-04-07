pas = input('Введите пароль ')

degit (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
letters = ('a' 'd','e', 'r', 'g', 'f', 's', 'k', 'l', 'j')

hasDigit = False
hasLetter = False
for sym in pas:
    if sym in Digit:
        hasDigit = True
    if sym in Letters:
        Letter = True
if len(pas) >= 8 and hasDigit == True and hasLetter == True:
    print('пароль годный')
else:
    print ('пароль плохой')
