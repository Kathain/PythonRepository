class Counter:
    counter = 0

    def start_from(self, x=0):
        if x != 0:
            self.counter = x

    def increment(self):
        self.counter+=1

    def display(self):
        print('Текущее значение счетчика =', self.counter)

    def reset(self):
        self.counter = 0
