import turtle

turtle.Screen().bgcolor("#27EEF5")
turtle.Screen().setup(500,500)

polygon=turtle.Turtle()
num_side=10
length=100
angle=360.0 / num_side
for i in range(num_side):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()