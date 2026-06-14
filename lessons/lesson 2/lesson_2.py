from unittest import TestCase
#1
is_sunny = True
is_warm = True
if is_sunny==True and is_warm==True:
    print('можна идти гулять')
else:
    print('лучше оставаться дома')
if is_sunny==True or is_warm==True:
    print('Можна одеть футболку')
else:
    print('лучше одень курточку')

#2
match "Среда":
    case "Понедедьник" | "Вторник" | "Среда" | "Четверг"|"Пятница":
        print('Рабочий день')
    case "Суббота" | "Воскресеньье":
        print('Выходной день')
    case _:
        print('неизвестный день')



