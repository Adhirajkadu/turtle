import turtle

turtle.bgcolor("black")
colors=["red", "blue", "orange", "green", "purple", "yellow"]
p=turtle.Pen()

for i in range(360):
    p.pencolor(colors[i%6])
    p.width(i/100 +1)
    p.forward(i)
    p.left(59)