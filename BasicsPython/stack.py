class Stack:

    empty_list = True

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print('Empty Stack')
        else:
            return self.values.pop(-1)

    def peek(self):
        if len(self.values) == 0:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        if len(self.values) == 0:
            self.empty_list = True
        else:
            self.empty_list = False
        return self.empty_list

    def size(self):
        return len(self.values)

if __name__ == '__main__':
    s = Stack()
    s.peek()  # распечатает 'Empty Stack'
    s.push('cat')  # кладем элемент 'cat' на вершину стека
    print(s.values)
    s.push('dog')  # кладем элемент 'dog' на вершину стека
    print(s.values)
    print(s.peek())  # распечатает 'dog'
    s.push(True)  # кладем элемент True на вершину стека
    print(s.values)
    print(s.size())  # распечатает 3
    print(s.is_empty())  # распечатает False
    s.push(777)  # кладем элемент 777 на вершину стека
    print(s.values)
    print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
    print(s.values)
    print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
    print(s.size())  # распечатает 2
