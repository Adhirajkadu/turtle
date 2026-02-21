import turtle

turtle.Screen().bgcolor("#27EEF5")
turtle.Screen().setup(500,500)

square=turtle.Turtle()
num_side=4
length=100
angle=360.0 / num_side
for i in range(num_side):
    square.forward(length)
    square.right(angle)
turtle.done()