import turtle
import os

wnd = turtle.Screen()

wnd.title("Pong by vioviooo")
wnd.bgcolor("blue")

wnd.setup(width = 800, height = 600)
wnd.tracer(0) # stops window from updating 

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # for not drawing lines
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # for not drawing lines
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # max possible speed
ball.shape("circle")
ball.color("white")
ball.penup() # for not drawing lines
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Score
score_a = 0
score_b = 0

# Pen = for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # for not drawing lines
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# python3 py-game.py

# Functions for Paddle A
def paddle_a_up():
    y = paddle_a.ycor() # get
    y += 20 # plus
    paddle_a.sety(y) # set

def paddle_a_down():
    y = paddle_a.ycor() # get
    y -= 20 # plus
    paddle_a.sety(y) # set

# Functions for Paddle B
def paddle_b_up():
    y = paddle_b.ycor() # get
    y += 20 # plus
    paddle_b.sety(y) # set

def paddle_b_down():
    y = paddle_b.ycor() # get
    y -= 20 # plus
    paddle_b.sety(y) # set

# Keyboard binding
wnd.listen()

wnd.onkeypress(paddle_a_up, "w")
wnd.onkeypress(paddle_a_down, "s")

wnd.onkeypress(paddle_b_up, "i")
wnd.onkeypress(paddle_b_down, "k")

# main game loop
while True:
    wnd.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border ? Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
    
    # Paddle and ball interaction
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")


