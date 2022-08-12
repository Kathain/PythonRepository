class Point:
    ant = False
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, obj):
        if isinstance(obj, Point):
            ant = True
            if ant is True:
                res1 = ((self.x - obj.x) ** 2 + (self.y - obj.x) ** 2) ** 0.5
                return res1
            else:
                print('Передана не точка')

if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    p1.set_coordinates(1, 2)
    p2.set_coordinates(4, 6)
    d = p1.get_distance(p2)  # вернёт 5.0
    p1.get_distance(10)  # Распечатает "Передана не точка"

