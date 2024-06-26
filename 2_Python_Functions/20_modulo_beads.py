# This program draws a string of beads.

import turtle

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    if n % 2 == 0:
        t.color("red")
    else:
        t.color("blue")
    bead(t)
    t.forward(40)

input()