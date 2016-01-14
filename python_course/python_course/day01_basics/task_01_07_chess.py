import turtle

turtle.speed('fastest')

width = int(input('Enter width: '))
height = int(input('Enter height: '))
side = int(input('Enter side size (integer): '))


def print_row(j):
    for i in range(width):
        if (i + j) % 2 == 0:
            turtle.begin_fill()

        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

        turtle.end_fill()
        turtle.forward(side)

for i in range(height):
    print_row(i)

    turtle.penup()
    turtle.setpos(0, -(side * (i + 1)))
    turtle.pendown()

turtle.exitonclick()