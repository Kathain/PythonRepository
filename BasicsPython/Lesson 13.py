name = "Привет мир!"
for j in name:  # создали цикл
    print(j)

for b in range(1, 5):  # выведет строчку привет мир - 4 раза!
    print(name)

h = 1

while h <= 10:  # цикл с условием
    if h != 5:
        print(h)
    h += 1
    continue
    # столкнется с 5 и потом продолжит цикл