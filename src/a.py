import turtle
import winsound

wn = turtle.Screen()
wn.title("PingPongWithU!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Background music
# winsound.PlaySound('同じ空はどこにも無い - H.B STUDIO.mp3', winsound.SND_FILENAME)

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -ball.dy
        pen.clear()
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -ball.dy
        pen.clear()
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        pen.clear()
        score_b -= 5
        if score_b < 0:
            score_b = 0
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        pen.clear()
        score_a -= 5
        if score_a < 0:
            score_a = 0
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})
        
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx = -ball.dx
        score_a += 1
        pen.clear()
        pen.write("Play A: {} Player B: {}".format(score_a, score_b), align="center", font={"consolas", 24, "normal"})
