print(tuple([45, 44, 11, 434]))        # преобразовывает из списка в кортеж
print(list((33, 44, 4232, 44, )))       # из кортежа наоборот в список

dict = {'apple': 'red', 'banane': 'yellow', 'lemon': 'yellow'}

dict["lemon"] = "green"       # изменит значение у ключа
print(dict)

for k in dict.keys():         # цикл выведет список всех ключей (это то что слева от двоеточия)
    print(k)

for k in dict.values():          # вывел только значения из словаря
    print(k)

for k in dict.items():       # выведет все
    print(k)

print(dict["lemon"])          # выведет значение ключа

del(dict['banane'])             # удалит ключ со значением
print(dict)
