names1 = ['kira', 'ura', 'oleg']

n = names1.index('ura')        # показывает индекс нужного нам элемента
print(n)



names1.append('Попугай1')    # добавляет методом еще один элемент в наш список
print(names1)

names1.pop()      # этот метод удаляет последний элемент из нашего списка
print(names1)
print(len(names1))           #  показывает длинну списка нашего