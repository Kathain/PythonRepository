class Cat:
    __shared_attr = {
        'name': 'Alex',
        'age': '2 years',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr



