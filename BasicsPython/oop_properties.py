class Cat:
    breed = "Siam"
    is_from_street = False
    color_of_eyes = "Green"

    def push_on_street(self):
        self.is_from_street = True


if __name__ == '__main__':
    Alex = Cat()
    print(Alex.breed)
    Alex.breed = "Noname"
    print(Alex.breed)
    Cesar = Cat()
    print(Cesar.breed)
    Cesar.push_on_street()
    print(Cesar.is_from_street)
    print(Alex.is_from_street)