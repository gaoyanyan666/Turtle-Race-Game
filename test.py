import turtle
import random
import math

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

t.speed(0)
t.penup()
t.goto(0, 0)

distance = 100 * math.pi
startLineX = 50
startLineYs = [-125, -175, -225]
colors = ['blue', 'orange', 'green']
found_winner = False

# Draw concentric circles
circle_radius = [100, 150, 200, 250]
for radius in circle_radius:
    t.goto(50, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()


def create_turtle_player(color, startx, starty):
    player = turtle.Turtle()
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.goto(startx, starty)
    player.pendown()
    return player


# Creating turtle players
players = [create_turtle_player(color, startLineX, starty) for color, starty in zip(colors, startLineYs)]


def calculate_central_angle(distance, radius):
    if radius <= 0 or distance <= 0:
        raise ValueError("Both radius and arc length must be positive values.")
    else:
        central_angle = distance * 360 / radius
        return central_angle


# Function to handle the race
def race_turtle(player, radius):
    central_angle = calculate_central_angle(distance, radius)
    player.circle(radius + 25, central_angle)


# Function to run each turtle with a delay
def run_turtle_with_delay(player, radius, delay):
    turtle.ontimer(lambda: race_turtle(player, radius), t=delay)


# Simulating the race
for player, radius in zip(players, circle_radius):
    delay = 100  # Convert to milliseconds
    run_turtle_with_delay(player, radius, delay)

turtle.done()
