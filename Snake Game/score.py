from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score}",False, 'center', ('Arial', 14, 'normal'))

    def update(self):
        '''Podfunkcja uzywana do akutalizacji wyniku'''
        self.write(f"Score: {self.score}", False, 'center', ('Arial', 14, 'normal'))

    def amend(self, ):
        '''funkcja dodaje nam punkt za konsumpcje, czysci poprzedni wynik i wyswietla nowy'''
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        '''funkcja wyswietla napis Game Over'''
        self.goto(0,0)
        self.write('Game Over', False, 'center', ('Arial', 24, 'normal'))


