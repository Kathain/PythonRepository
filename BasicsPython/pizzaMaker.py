class PizzaMaker:
    def __make_pepperoni(self):
        print('I make a pepperoni')

    def _make_barbecue(self):
        print('Make a barbecue ')

if __name__ == '__main__':
    maker = PizzaMaker()
    maker._make_barbecue()
    maker._PizzaMaker__make_pepperoni()