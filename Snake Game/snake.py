from turtle import Turtle
'''Pozycje startowe naszego węża w tuple (3 kwadraty po 20 pix kazdy)'''
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        '''Tworzy pusta liste dla naszych kwadratow'''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''Tworzymy węża, jej miejsce startowe, ksztalt i kolor'''
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)



    def move(self):
        '''Sprawia, że ostatni kwadrat zaciaga pozycje przedostatniego a przedostatni pierwszego + pierwszy rusza sie o 20 pixeli'''

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def add_segment(self, position):
        '''Funkcja odpowiadajaca za dodanie nowego elementu'''
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extent(self):
        '''Funkcja odpowiadajaca za przedluzenie weza na jego koncu'''
        self.add_segment(self.segments[-1].position())

