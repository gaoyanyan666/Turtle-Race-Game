'''
create antoher race that moves the turtles in diffferent lanes on a circular track. Use 4 concentric circles to construct the track and have each turtle race within the track between the circles.

l: race distance
s: speed in range(1,5)
r: radius

round is the rounds that turtle needs to run


l = 2(math.pi)r * round
round = l/[turtle.radians()*r]
extend=(180L)/(πr)


## Function to calculate the number of steps based on the distance
#def calculate_steps(radius):
#    #circumference = 2 * math.pi * radius
#    rounds =1 #distance / circumference
#    steps = int(rounds * 360)  # Convert rounds to steps (degrees)
#    return steps

 
## Function to make a turtle move in a circle
#def move_in_circle(turtle, radius, steps):
#    circumference = 2 * math.pi * radius
#    step_length = circumference / steps
    
#    for _ in range(steps):
#        turtle.forward(step_length)
#        turtle.left(360 / steps)

'''


import turtle
import random
import math

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

t.speed(0)
t.penup()
t.goto(0, 0)

distance= 30 * math.pi
startLineX=50
startLineYs = [-125,-175,-225]
colors=['blue','orange','green']
found_winner = False

# Draw concentric circles
circle_radius = [100, 150, 200, 250]
for radius in circle_radius:
    t.goto(50, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()


def createTurtlePlayer(color, startx, starty): 
	player=turtle.Turtle()
	player.color(color) # set the color of turtle
	player.shape("turtle") #set the shape as turtle
	player.penup() #pen moves up
	player.goto(startx, starty) #place player at mentioned position on race track.
	player.pendown() #pen placed down
  
	return player #returns the turtle player object.

# Creating turtle players
players = [createTurtlePlayer(color, startLineX, starty) for color, starty in zip(colors, startLineYs)]


def calculate_central_angle(distance, radius):
    if radius <= 0 or distance <= 0:
        raise ValueError("Both radius and arc length must be positive values.")
    else:
        central_angle = distance * 360 / radius
        return central_angle


# Function to handle the race
def race_turtle(turtle,radius):
    turtle.speed(random.randint(5, 10)) 
    central_angle = calculate_central_angle(distance, radius)
    #move_in_circle(turtle, radius, steps)
    #x,y = turtle.pos()
    #print(turtle.pos()) 
    turtle.circle(radius+25,central_angle)
 

# Simulating the race
for i in range(1):
    for player,radius in  zip(players,circle_radius) :
        race_turtle(player,radius)

turtle.done()

