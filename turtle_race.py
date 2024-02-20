import play
import random, turtle

foundWinner = False
myscreen= turtle.Screen()

myscreen.bgcolor('light blue')
myscreen.setup(1.0,1.0)
myscreen.title('Turtle Race Game')

pen=turtle.Turtle()

pen.speed(0) # so it moves with fastest speed
pen.penup() #pen goes up as we don't want to draw on line.
pen.goto(-250,250) #this is x and y position from center of the screen
pen.pendown() # pen placed down again


for i in range(0,11): # this will run from 1 to 10 
    pen.write(i,font=('Arial',10)) #writing the race track number before each line
    pen.setheading(-90) #this will point pen in downward direction
    for j in range (5):
        pen.penup() #pen goes up as we don't want to draw on line'
        pen.forward(40)
        pen.pendown()
        pen.forward(40)
    if i==10: # this if condition will be true only if the iterating variable is 10 
        pen.write(" FINISH",font=('Arial',14))
    pen.penup() #pen goes up as we don't want to draw on line
    pen.backward(400) #pen points in right direction
    pen.setheading(0)
    pen.forward(50)  #space of 50 pixes between each line
    #pen.down() #pen down again

finishLineX=250

def createTurtlePlayer(color, startx, starty): 
	player=turtle.Turtle()
	player.color(color) # set the color of turtle
	player.shape("turtle") #set the shape as turtle
	player.penup() #pen moves up
	player.goto(startx, starty) #place player at mentioned position on race track.
	player.pendown() #pen placed down
	return player #returns the turtle player object.

# Creating turtle players
players = [
    createTurtlePlayer('purple', -270, 200),
    createTurtlePlayer('red', -270, 150),
    createTurtlePlayer('blue', -270, 100),
    createTurtlePlayer('orange', -270, 50),
    createTurtlePlayer('green', -270, 0)
]

# Variable to track whether each turtle completed one lap
lap_completed = {player: False for player in players}

# Function to handle the race
def race_turtle(turtle):
    if not lap_completed[turtle]:
        turtle.forward(random.randint(5, 10))

        if turtle.xcor() >= finishLineX:
            turtle.setheading(180)  # Turn around when reaching the right side

        if turtle.xcor() <= -270 and turtle.heading() == 180:
            turtle.setheading(0)  # Turn around when reaching the left side

            # Mark lap as completed when turning around to the starting line
            lap_completed[turtle] = True

# Simulating the race
while not all(lap_completed[player] for player in players):
    for player in players:
        race_turtle(player)
        
    # Check if any turtle has completed one lap
    if any(lap_completed[player] for player in players):
        for player in players:
            if lap_completed[player]:
                if foundWinner == False :
                    player.write(' I am the winner!!', font=('Arial', 30))
                    foundWinner = True

turtle.done()
play.start_program()