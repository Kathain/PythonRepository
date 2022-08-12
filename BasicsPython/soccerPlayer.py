class SoccerPlayer:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, count_of_goals = 1):
        self.goals = self.goals + count_of_goals

    def make_assist(self, count_of_assists = 1):
        self.assists = self.assists + count_of_assists

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")

        #<Фамилия> <Имя> - голы: <goals>, передачи: <assists>
        #"Messi Leo - голы: 700, передачи: 500"

if __name__ == '__main__':
    leo = SoccerPlayer('Leo', 'Messi')
    leo.score(700)
    leo.make_assist(500)
    leo.statistics()  # выводит "Messi Leo - голы: 700, передачи: 500"
    kokorin = SoccerPlayer('Alex', 'Kokorin')
    kokorin.score()
    kokorin.statistics()  # выводит "Kokorin Alex - голы: 1, передачи: 0"





