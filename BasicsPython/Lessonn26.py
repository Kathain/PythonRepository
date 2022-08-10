a = 20
b = 30

def calculator(a, b):
    product = a * b
    if product > 1000:
        return product
    else:
        product2 = a + b
        return product2

number = calculator(40, 30)
print(number)

