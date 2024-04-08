import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star
    
for angle in [180, 135, 90, 45, 0, -45, -90, -135, -180]:
    star("violet", 5, 50, angle, 100)

for angle in [315, 270, 225, 180, 135, 90, 45, 0]:
    star("light blue", 5, 30, angle, 60)

for color in ["violet", "pink", "white"]: # Draw three stars with different colors.
    star(color, 5, 50, 0, 0)

for length in [50, 100, 200]:
    star("red", 5, length, 0, 0) # Draw three stars with different sizes.
    
for distance in [0, 70, 140]:
    star("red", 5, 50, 0, distance) # Draw three stars at different distances from the starting location.

input()