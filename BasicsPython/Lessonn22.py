# форматирование строк
name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)    #  используем метод формат и как бы заполнители 0 и 1
print(name_and_age)

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'.format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(week_days)


# тут работаем с числами с остатком и как можно сделать красивые таблицы
float_result = 1000 / 7
print(float_result)
print('The result of division is {0:1.3f}'.format(float_result))
print('''                       
{0:10.2f}{1:10.2f}{2:10.2f}
{3:10.2f}{4:10.2f}{5:10.2f}
{6:10.2f}{7:10.2f}{8:10.2f}
'''.format(1.4578, 345.2342342, 34.123112, 12.23232 , 1.4578, 345.2342342, 34.123112, 12.23232, 12.23232))
# :10 это пробел .2f - два это сколько знаков после запятой а f то что это тип float

new_name = 'Jack'
new_age = 23
new_name_and_age = f'My name is {new_name}. I\'m {new_age} years old.'   # новый способ форматирования (просто добавь f в начало)
print(new_name_and_age)

print('My name is %s. I\'m %d years old' % (new_name, new_age))       # уже старый метод который лучше не использовать



print('''
 {0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f} 
 {4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format(34.2344, 1234.23,1.45778, 345.232352,
           1.45778, 345.232352, 34.2344, 1234.23))

