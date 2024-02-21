import turtle
import random

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

t.speed(0)
t.penup()
t.goto(0, 0)

startLineX = 50
startLineYs = [-125,-175,-225]
colors=['blue','orange','green']
found_winner = False

# Draw concentric circles
circle_radius = [100, 150, 200, 250]
for radius in circle_radius:
    t.goto(startLineX, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()


def createTurtlePlayer(color, startx, starty): 
    player = turtle.Turtle()
    player.color(color)  # set the color of turtle
    player.shape("turtle")  # set the shape as turtle
    player.penup()  # pen moves up
    player.goto(startx, starty)  # place player at mentioned position on the race track.
    player.pendown()  # pen placed down
  
    return player  # returns the turtle player object.

# Creating turtle players
players = [createTurtlePlayer(color, startLineX, starty) for color, starty in zip(colors, startLineYs)]


# Variable to track whether each turtle completed one lap
lap_completed = {player: False for player in players}

# Function to handle the race
def race_turtle(turtle, radius):
    turtle.circle(radius + 25)
    turtle.speed(random.randint(1, 10))
        
    if turtle.xcor() == startLineX and turtle.ycor() == startLineY:
        lap_completed[turtle] = True

# Simulating the race
racing = True
while racing:
    for player, radius in zip(players, circle_radius):
        race_turtle(player, radius)

    # Check if all turtles completed one lap
    if all(lap_completed[player] for player in players):
        racing = False

turtle.done()

