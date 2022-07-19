import turtle
from pygame import mixer

# Screen
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the screen from refreshing so the game will run faster

# Score
score_a = 0
score_b = 0

# Sound
mixer.init()
sound = mixer.Sound("E:/Computer stuff - BUp/Python Projects/pyprojects/pong/bounce.wav")

# Paddle A
# an object (turtle is the name of the module, Turtle is the name of the class)
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set the speed to max
paddle_a.shape('square') # defult square is 20px by 20px
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.color('white')
paddle_a.penup() # no drawing a line
paddle_a.goto(-350, 0) # paddle A is to the far left (-350) center (0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set the speed to max
paddle_b.shape('square') # defult square is 20px by 20px
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.color('white')
paddle_b.penup() # no drawing a line
paddle_b.goto(350, 0) # paddle B is to the far right (350) center (0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # set the speed to max
ball.shape('circle') # defult size is 20px by 20px
ball.color('white')
ball.penup() # no drawing a line
ball.goto(0, 0) # the ball is in the center'
# For moving 
ball.dx= 0.2  # x changes by this px (This speed depends on how fast your computer is, if it's too fast, the ball just disapears. You should play around with it to find a good speed)
ball.dy= -0.2  # y changes by this px

# Pen (Score board)
pen = turtle.Turtle()
pen.speed(0) # animation speed, not movement speed
pen.color('white')
pen.penup() # without it there'll be a line moving up
pen.hideturtle() #no need to see the pen
pen.goto(0, 260) #on top of the window
pen.write('Player A: 0  Player B: 0', align='center', font=('courier', 24, 'normal'))

# Functions to move the paddles
# Paddle A
def paddle_a_up():
    # first need to know the y cordinates of the paddle
    y = paddle_a.ycor()
    # y increases as we go up
    y += 20 # add 20px
    # move the paddle by setting the new y
    y = paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    # y decreases as we go down
    y -= 20 # subtrack 20px
    y = paddle_a.sety(y)

# Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    y = paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    y = paddle_b.sety(y)

# Keyboard Binding
wn.listen() #wait for keyboard input
wn.onkeypress(paddle_a_up, 'w') #if 'w' is pressed, use paddle_a_up function
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')  #up arrow key
wn.onkeypress(paddle_b_down, 'Down')


# Main Game Loop
while True:
    wn.update() # whenever the loop runs, we need to update the screen
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking (So the ball will bounce off the border, not out of the screen)
    # Top border 
    if ball.ycor() > 290:  #the height is 600 and the ball is in the middle so there is only 290px above the ball.
        ball.sety(290)
        ball.dy *= -1 # reverse the direction
        sound.play()

    # Bottom border 
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse the direction
        sound.play()

    # Right border
    if ball.xcor() > 390: 
        ball.goto(0, 0)  # back to the center
        ball.dx *= -1
        score_a +=1 #if the ball goes off the right border, player A gets a score.
        # clear the board ro make room for the new score
        pen.clear()
        # print the new score
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('courier', 24, 'normal'))
    
    # Left border 
    if ball.xcor() < -390: 
        ball.goto(0, 0)  # back to the center
        ball.dx *= -1
        score_b +=1 #if the ball goes off the left border, player B gets a score.
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('courier', 24, 'normal'))
        
    # Paddle and ball collisions
    # with Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        sound.play()

    # with Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        sound.play()