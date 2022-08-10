ages = [1, 18, 20, 30, 50]
for age in ages:
    if age <= 18:
        print("NO")
    elif age >= 19 and age < 30:
        print("Adult")
    else:
        print("YOURE OLD")