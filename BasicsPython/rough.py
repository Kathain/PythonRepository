def check_password(p):
    count_digit = 0
    count_upper = 0
    count_characters = 0
    count_len = 0
    for s in p:
        if s.isdigit():
            count_digit += 1
    for i in p:
        if i.isupper():
            count_upper += 1
    for n in p:
        if n.isalnum():
            count_characters += 1
    for l in p:
        if len(p) <= 10:
            count_len += 1
    print('count', count_len)

    if count_digit <= 3:
        print('OK')
    else:
        print('NO OK')
    if count_upper >= 1:
        print('Ok')
    else:
        print('NO')

    if count_characters >= 1:
        print('OK')
    else:
        print('NO')
    if count_len <= 10:
        print('OK')
    else:
        print('NO')


check_password('KKKn332')









