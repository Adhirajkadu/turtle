import turtle

turtle.Screen().bgcolor("#c395db")
s=turtle.Turtle()

#creating 1st star
s.forward(100)
s.left(120)

s.forward(100)
s.left(120)
s.forward(100)

#adjesting position for second star
s.penup()
s.right(150)
s.forward(50)

#drawing 2nd triangle
s.pendown()
s.right(90)
s.forward(100)

s.right(120)
s.forward(100)

s.right(120)
s.forward(100)

turtle.done()