first_name = 'Jake'                   # строки просто так не изменяются и не редактируются (мы не можем заменить
                                       # легко одну букву на другую)
print(first_name[2])

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1]
print(last_letter)

# тут  конкатинация, соединение строк - Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello '
greeting = greeting + 'Python!'
print(greeting)
# Multiplication    - умножение

yummy = 'Yum '
print(yummy * 3)

print(yummy.upper())        # делает буквы большими
print(yummy.lower())        # делает буквы маленькими

long_string = 'This is the longer string'
print(long_string.split())          # разделяет по словам

