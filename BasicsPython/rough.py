class Point:
    def set_coordinates(self, x, y):
        setattr(self,'x_coordinate', x)
        setattr(self,'y_coordinate', y)
    def get_distance(self, obj):
        if not isinstance(obj, Point):
            print('Передана не точка')
        else:
            res1 = ((self.x_coordinate - obj.x_coordinate)**2 + (self.y_coordinate - obj.y_coordinate)**2)**0.5
            return res1

if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    p1.set_coordinates(1, 2)
    print(p1.x_coordinate)
    p2.set_coordinates(4, 6)
    d = p1.get_distance(p2)  # вернёт 5.0
    p1.get_distance(10)  # Распечатает "Передана не точка"