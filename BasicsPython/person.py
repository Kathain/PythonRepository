class Person:
    def __init__(self, first_name , last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        if self.age < 18:
            return('False')
        else:
            return('True')

if __name__ == '__main__':
    p1 = Person('Jimi', 'Hendrix', 55)
    print(p1.full_name())  # выводит "Hendrix Jimi"
    print(p1.is_adult())  # выводит "True"