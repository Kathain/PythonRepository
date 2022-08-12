class Developer:
    list_programm_language = ['java']
    ready_work_at_home = True
    ammount_of_ram = 8

    def ram_improvement(self, size):
        if size == 0:
            print('Your computer is not improved')
        else:
            result = self.ammount_of_ram + size
            print(result)

    def learn_language(self,new_lng):
        self.list_programm_language.append(new_lng)
        print(self.list_programm_language)

    def go_to_theoffice(self):
        self.ready_work_at_home = True



if __name__ == '__main__':
    Kate = Developer()
    Kate.learn_language("C++")