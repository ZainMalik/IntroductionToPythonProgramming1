import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
t.width(20)

for step in range(100):
    angle = random.randint(1, 360)
    color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(10)

input()