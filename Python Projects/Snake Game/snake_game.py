''' Music from Pixabay'''

import turtle
import time
import random
from pygame import mixer

delay = 0.1
segments = [] # a list to make the snake body 

# Score
score = 0
high_score = 0

# Sound
mixer.init()
sound_eat = mixer.Sound("C:/Users/Yassi/Desktop/Snake Game/eat.mp3")
sound_lose = mixer.Sound("C:/Users/Yassi/Desktop/Snake Game/lose.mp3")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square') # doens't really matter b/c we're gonna hide it. 
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align='center',font=('Courier', 24, 'normal'))

# setting up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the the screen updates --> faster program

# Snake Head
head = turtle.Turtle()
head.speed(0) # animation zero of the object, 0 is the fastest
head.shape('square')
head.color('black')
head.penup() # no drawn line
head.goto(0, 0) # in the middle
head.direction = 'stop' # stop in the middle until told to move!

# Snake Food!
food = turtle.Turtle()
food.speed(0) # animation zero of the object, 0 is the fastest
food.shape('circle')
food.color('red')
food.penup() # no drawn line
food.goto(0, 100) # in the middle


# Functions
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20) # moves up by 20px each time

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == 'right':
        head.setx(head.xcor() + 20)

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def set_score():
    pen.clear()
    pen.write('Score: {}   High Score:{}'.format(score, high_score), align='center',font=('Courier', 24, 'normal'))

# Keyboard Binding
wn.listen()
wn.onkeypress(go_up,'Up')  # Up, Down, Left, Right are the arrow keys and need to be capitilized.
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

# Main game loop
while True:
    wn.update() # b/c we diactivated the  tracer, we need to update the screen

    # Check for a collision with the borders
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        sound_lose.play()
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # moving it off the screen, b/c there is no delete option.
        segments.clear()

        # reset the score:
        score = 0
        set_score()

        # reset the delay
        delay = 0.1

    # Check for a collision with the food
    if head.distance(food) < 20: #each turtle shape is 20px by defult
        sound_eat.play()
        # move the food to a random spot on the screen
        x = random.randint(-280, 280) # screen is 600 wide (-300 to 300)
        y = random.randint (-280, 270)  #270 so it won't be on the Score, -280 so the food will not go off the screen
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0) # animation zero of the object, 0 is the fastest
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup() # no drawn line
        segments.append(new_segment)

        #shorten the delay to speed up the game
        delay -= 0.001
        
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        set_score()

    # add the segments in reverse order
    for i in range (len(segments)-1, 0, -1): # from the last segment upto segment 0, with -1 steps
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    # this for loop runs only if the len(segment) is bigger than 1 (len(segments)-1 can't be 0) so if there is only one segment, we need to move it separately.
    # move segment 0 to where the head is.
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            sound_lose.play()
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000) # moving it off the screen, b/c there is no delete option.
            segments.clear()

            # reset the score
            score = 0
            set_score()        

    time.sleep(delay) # to slow down the moving so we can see the turtle

wn.mainloop() # to keep the window open