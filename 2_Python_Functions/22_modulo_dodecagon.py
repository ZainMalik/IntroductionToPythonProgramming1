import turtle

zain = turtle.Turtle()
zain.width(5)

for n in range(12):
    zain.color("gray")
    if n % 3 == 0:
        zain.color("red")
    if n % 3 == 1:
        zain.color("orange")
    if n % 3 == 2:
        zain.color("yellow")
    zain.forward(50)
    zain.right(360/12)

input()