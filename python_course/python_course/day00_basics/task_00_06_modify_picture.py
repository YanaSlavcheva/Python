import turtle

i = 10
color_index = 0

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
turtle.color(colors[color_index])
turtle.speed('fastest')
turtle.pensize(5)

while True:
    turtle.left(i % 48)
    turtle.forward(10)

    if i % 48 == 0:
        if color_index == len(colors) - 1:
            color_index = 0
        else:
            color_index += 1

    turtle.color(colors[color_index])

    i += 1

    if i == 730:
        break