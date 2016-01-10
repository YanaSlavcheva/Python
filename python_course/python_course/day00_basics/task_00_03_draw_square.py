import turtle

square_width = 100

screen = turtle.Screen()

turtle.speed('slow')

turtle.penup()
turtle.goto(-(square_width / 2), (square_width / 2))
turtle.pendown()

turtle.color('#FF69B4')
turtle.pensize(square_width // 10)

turtle.forward(square_width)
turtle.right(90)
turtle.forward(square_width)
turtle.right(90)
turtle.forward(square_width)
turtle.right(90)
turtle.forward(square_width)
turtle.right(90)

screen.exitonclick()






