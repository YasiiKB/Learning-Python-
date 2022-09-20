import turtle
import math
import os
import platform
from pygame import mixer 

# File Location
file_location = "C:/Users/Yassi/Desktop/Space Invaders/"

# Sound Module  (Only works with .wav)
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available!")

# Sound funcion
def play_sound(sound_file, time = 0):
    # Windows 
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # Mac
    else:
        os.system("afplay {}&".format(sound_file))
    # Repeat sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000)) # time is seconds, but t is in miliseconds so * 1000

# Set up Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic(file_location + "space_invaders_background.gif")
wn.tracer (0)  #shut down all the screen updates to speed up the program

# Register the Shapes
wn.register_shape(file_location + "player.gif")
wn.register_shape(file_location + "invader.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)  #the built-in animation speed. 0 is the fastest. 
border_pen.color("white")
border_pen.penup() 
border_pen.setposition(-280,-280)  # start drawing at the bottom left corner
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):  # 4 sides of the square
    border_pen.fd(560)  #space btw the window and sqaure
    border_pen.lt(90)  # go left 90 degrees b/c we're drawing a square
border_pen.hideturtle()

# Score
score = 0
# Draw the Score 
score_pen = turtle.Turtle()
score_pen.speed(0)  #0 is the fastest.
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-270,250)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.shape(file_location + "player.gif")
player.penup() # no need to draw anything
player.speed(0)
player.setposition(0, -250)  #x,y = center, bottom
player.setheading(90) # direction up 

# Moving Player   
player.speed = 0  # 15 pixels
# Move Left
def move_left():
    player.speed = -0.5   # play around to find a good speed
# Move Right
def move_right():
    player.speed = 0.5

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -270:  # Boundary Checking: so it won't move off the screen
        x = -270
    if x > 270: # so it won't move off the screen
        x = 270
    player.setx(x)

# Create multiple enemies
number_of_enemies = 30
enemies = []  # an empty list of enemies 
for i in range (number_of_enemies):  #add enemies to the list
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -230
enemy_start_y = 230
enemy_number = 0

for enemy in enemies:
    enemy.shape(file_location + "invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy number
    enemy_number += 1
    # Ten enemies in each line
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.1

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)  # not as big as the players
bullet.hideturtle()

bulletspeed = 4 # bullet is faster than other objects
# Define Bullet State
    # ready - ready to fire
    # fire - bullet is firing
bulletstate = "ready" # the beginning of the game

def fire_bullet():
    # Define bulletstate as global b/c we need to change it in the whole program
    global bulletstate
    if bulletstate == "ready":
        play_sound(file_location + "laser.wav")
        bulletstate = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    # Pythagorean theorem
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Create Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Play background Music
# play_sound(file_location +"background.wav", 119) --> Stops when a bullet is shot
# Another way of playing sound #
mixer.init()
bgsound = mixer.Sound(file_location +"background.wav")
bgsound.play()


# Main game loop
while True:
    wn.update() #to speed up the program
    move_player()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        # Move all the enemies down if one touches the border
        if enemy.xcor() > 265:
            for e in enemies:
                y = e.ycor()
                y -= 40 # move down
                e.sety(y)
            enemyspeed *= -1 # change direction (-2)

        if enemy.xcor() < -265: 
            for e in enemies: 
                y = e.ycor()
                y -= 40  # move down           
                e.sety(y)
            enemyspeed *= -1 # change direction (+2)

        # Check for collision between the enemy and the bullet
        if isCollision(bullet, enemy):
            play_sound(file_location + "explosion.wav")
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0, 5000)
            # Update Score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # Check for collision between the enemy and the player
        if isCollision(player, enemy):
            play_sound(file_location + "gameover.wav")
            player.hideturtle()
            enemy.hideturtle()
            # Write Game Over
            game_pen = turtle.Turtle()
            game_pen.speed(0)  #0 is the fastest.
            game_pen.color("red")
            game_pen.penup()
            game_pen.setposition(0,0)
            game_pen.write("GAME OVER!", False, align="center", font=("Arial", 50, "normal"))
            game_pen.hideturtle()
            break

    # Move the bullet if it's ready 
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    # Bourder Checking (checking if the bullet has gone to the top)
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"