n = int(input())
count = 0
while 0 < n <= 5:
    n = int(input())
    while n == 5:
        count = count + 1
        n = int(input())
print(count)



