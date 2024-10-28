'''import turtle
import random

loadWindow=turtle.Screen()

angana =turtle.pen()
#angana.color("red")
kshitiz=turtle.pen()
#kshitiz.color("Blue")
moomsies=turtle.pen()
#moomsies.color("#ff00ff")
piyush=turtle.pen()
#piyush.color("#00ffff")

angana.shape("turtle")
kshitiz.shape("circle")
moomsies.shape("square")
piyush.shape("triangle")

angana.left(90)
kshitiz.forward(-50)
kshitiz.left(90)
moomsies.forward(50)
moomsies.left(90)
piyush.forward(100)
piyush.left(90)

for x in range (100):
    a=random.randint(-5,30)
    k=random.randint(-5,30)
    m=random.randint(-5,30)
    p=random.randint(-5,30)

    angana.forward(a)
    kshitiz.forward(k)
    moomsies.forward(m)
    piyush.forward(p)

turtle.exitonclick()'''

import turtle
import random

# Set up the screen
loadWindow = turtle.Screen()

# Create turtle instances with different names
angana = turtle.Turtle()  # Changed to Turtle()
angana.color("red")
angana.shape("turtle")

kshitiz = turtle.Turtle()  # Changed to Turtle()
kshitiz.color("blue")
kshitiz.shape("circle")

moomsies = turtle.Turtle()  # Changed to Turtle()
moomsies.color("#ff00ff")
moomsies.shape("square")

piyush = turtle.Turtle()  # Changed to Turtle()
piyush.color("#00ffff")
piyush.shape("triangle")

# Set starting positions
angana.left(90)
kshitiz.forward(-50)
kshitiz.left(90)
moomsies.forward(50)
moomsies.left(90)
piyush.forward(100)
piyush.left(90)

# Random movement loop
for x in range(100):
    a = random.randint(-5, 30)
    k = random.randint(-5, 30)
    m = random.randint(-5, 30)
    p = random.randint(-5, 30)

    angana.forward(a)
    kshitiz.forward(k)
    moomsies.forward(m)
    piyush.forward(p)

# Wait for a click to exit
loadWindow.exitonclick()
