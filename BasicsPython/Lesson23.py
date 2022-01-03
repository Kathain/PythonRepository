# тут разбираем множество (тут не может быть двух одинаковых элементов)
rainbow_colors = {'red', 'orange', 'indigo', 'violet', 'green'}      # сюда помещается значение без ключей
print(rainbow_colors)
print(type(rainbow_colors))           # выводит тип переменной
empty_set = set()          # создаем пустое множество
print(empty_set)
print(type(empty_set))

number_list = [1, 44, 56]
text_tuples = ('sdfsd', 'sdsd', 'dsew', 'ewewew')
set_from_list = set(number_list)
set_from_tuples = set(text_tuples)
set_from_list.add(777)
set_from_tuples.add('helllooo')
print(set_from_list)
print(set_from_tuples)