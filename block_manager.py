from turtle import Turtle

RED="red"
ORANGE="orange"
GREEN="green"
BLUE="blue"

class Blocks(Turtle):
    def __init__(self):
        self.all_blocks =[]

        super().__init__()
        stop = 1
        x=-220
        y=390
        st=0
        while st <3:
            x = -220
            for _ in range(5):
                block = Turtle()
                block.penup()
                block.shape("square")
                block.color(RED)
                block.shapesize(stretch_wid=1,stretch_len=4)

                block.goto(x,y)
                x+=100
                self.all_blocks.append(block)

            x+=50
            y-=25
            #self.block.color("blue")
            st+=1


        self.ball=Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.goto(0,-180)

        self.ball_dx = 3
        self.ball_dy = 3







        self.board=Turtle()
        self.board.penup()
        self.board.shape("square")
        self.board.color("white")
        self.board.shapesize(stretch_wid=1, stretch_len=4)
        self.board.goto(0,-230)

        self.moving_left = False
        self.moving_right = False

        # --- Ball movement ---

    def move_ball(self):
        x = self.ball.xcor() + self.ball_dx
        y = self.ball.ycor() + self.ball_dy
        self.ball.goto(x, y)

        # Bounce off left/right walls
        if x > 260 or x < -260:
            self.ball_dx *= -1

        # Bounce off top
        if y > 390:
            self.ball_dy *= -1

        # Bounce off paddle
        if (self.ball.ycor() < -210 and self.ball.ycor() > -230 and
                self.board.xcor() - 50 < self.ball.xcor() < self.board.xcor() + 50):
            self.ball_dy *= -1

        # Reset if ball falls below paddle
        if y < -400:
            self.ball.goto(0, -180)
            self.ball_dx = 3
            self.ball_dy = 3

        self.check_block_collision()

    def go_right(self):
       if self.board.xcor() < 220:
            ##new_x = self.xcor() + 30
           self.board.setx(self.board.xcor()+35)

    def go_left(self):
        if self.board.xcor() > -220:
            ##new_x = self.xcor() - 30
            self.board.setx(self.board.xcor()-35)

    #def start_move_left(self):
        #self.moving_left = True

    #def start_move_right(self):
        #self.moving_right = True

    #def stop_move_left(self):
        #self.moving_left = False

    #def stop_move_right(self):
        #self.moving_right = False

    def update_paddle(self):
        if self.moving_left and self.board.xcor() > -220:
            self.board.setx(self.board.xcor() - 10)
        if self.moving_right and self.board.xcor() < 220:
            self.board.setx(self.board.xcor() + 10)

    def check_block_collision(self):
        for block in self.all_blocks:
            if self.ball.distance(block) < 30:
                block.hideturtle()
                self.all_blocks.remove(block)
                self.ball_dy *= -1
                break
