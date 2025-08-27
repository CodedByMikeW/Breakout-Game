import turtle
from turtle import Screen,Turtle
from block_manager import Blocks
import time

block_manager=Blocks()
screen = Screen()
screen.title("Breakout Game")
screen.setup(width=550,height=800)
screen.bgcolor("black")
screen.tracer(0)
game_on=True
#while game_on:
#block_.create_block()
#turtle.color("red")

#block_.go_right()

screen.listen()
#screen.onkey(block_manager.start_move_right, "d")
#screen.onkey(block_manager.start_move_left, "a")
#screen.onkeyrelease(block_manager.stop_move_right, "d")
#screen.onkeyrelease(block_manager.stop_move_left, "a")
screen.onkey(block_manager.go_right, "d")
screen.onkey(block_manager.go_left, "a")
screen.onkey(block_manager.go_right, "Right")
screen.onkey(block_manager.go_left, "Left")

while game_on:
    #orginal 0.02
    time.sleep(0.005)  # Smooth animation
    block_manager.update_paddle()  # Paddle continuous movement
    block_manager.move_ball()  # Move ball and handle bounces
    screen.update()



screen.exitonclick()
