import random
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

#screen attributes
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')

#tracer wylacza animacje pojedynczego elementu (przy wartosci 0)
screen.tracer(0)

#przywolanie obiektow ze stworzonych klas
snake = Snake()
food = Food()
score = Score()

#wlaczenie wychwytywania klawiszy + zmapowanie ich dzialania
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

#Stworzenie switcha konczacego gre + opoznienie ekranu dla plynnosci animacji
is_on = True
while is_on == True:
    screen.update()
    time.sleep(0.10)
    snake.move()
#sprawdzanie kolizji weza z jedzeniem/ kropką
    if snake.head.distance(food) < 15:
        food.refresh()
        score.amend()
        snake.extent()
#wykryj kolizje ze sciana
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        score.game_over()

#blok wykrywajacy kolizje z cialem weza
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()

screen.exitonclick()