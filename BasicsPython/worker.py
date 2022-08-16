class Worker:
    def __init__(self,name,salary,gender,passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')

persons = [
        ('Allison Hill', 334053, 'M', '1635644202'),
        ('Megan Mcclain', 191161, 'F', '2101101595'),
        ('Brandon Hall', 731262, 'M', '6054749119'),
        ('Michelle Miles', 539898, 'M', '1355368461'),
        ('Donald Booth', 895667, 'M', '7736670978'),
        ('Gina Moore', 900581, 'F', '7018476624'),
        ('James Howard', 460663, 'F', '5461900982'),
        ('Monica Herrera', 496922, 'M', '2955495768'),
        ('Sandra Montgomery', 479201, 'M', '5111859731'),
        ('Amber Perez', 403445, 'M', '0602870126')
    ]
worker_objects = []

for p in persons:
    worker_objects.append(Worker(p[0], p[1], p[2], p[3]))

for w in worker_objects:
    w.get_info()

if __name__ == '__main__':
    bob = Worker('Bob Moore', 330000, 'M', '1635777202')
    bob.get_info()  # печатает "Worker Bob Moore; passport-1635777202"



