import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

t.speed(10)
t.penup()
t.goto(-200, 80)

for step in range(1):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()

    # Draw dashed line
    for _ in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

    t.penup()
    t.backward(170)
    t.left(90)
    t.forward(20)
   
day=turtle.Turtle()
day.penup()
day.goto(-220,50)
day.color('red')
day.shape('turtle')
day.pendown()
for _ in range(10):
  day.right(36)

jack=turtle.Turtle()
jack.penup()
jack.goto(-220,25)
jack.color('green')
jack.shape('turtle')
jack.pendown()
for _ in range(10):
  jack.right(36)
 
cool=turtle.Turtle()
cool.penup()
cool.goto(-220,-5)
cool.color('purple')
cool.shape('turtle')
cool.pendown()
for _ in range(10):
  cool.right(36)

umm=turtle.Turtle()
umm.penup()
umm.goto(-220,-30)
umm.color('blue')
umm.shape('turtle')
umm.pendown()
for _ in range(10):
  umm.right(36)

simple=turtle.Turtle()
simple.penup()
simple.goto(-220,-55)
simple.color('black')
simple.shape('turtle')
simple.pendown()
simple.pendown()
for _ in range(10):
  simple.right(36)

def race():
  for _ in range(150):
    day.forward(random.randint(1,5))
    umm.forward(random.randint(1,5))
    simple.forward(random.randint(1,5))
    jack.forward(random.randint(1,5))
    cool.forward(random.randint(1,5))

race()

if day.xcor() >= 190:
  for _ in range(5):
    day.right(36)

if umm.xcor() >= 190:
  for _ in range(5):
    umm.right(36)

if simple.xcor() >= 190:
  for _ in range(5):
    simple.right(36)

if jack.xcor() >= 190:
  for _ in range(5):
    jack.right(36)

if cool.xcor() >= 190:
  for _ in range(5):
    cool.right(36)

race()

turtle.done()