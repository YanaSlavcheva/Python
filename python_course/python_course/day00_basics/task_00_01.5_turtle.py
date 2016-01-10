import turtle

turtle.speed('fastest')

colors = ['red', 'green', 'blue', 'purple']

for a in range(4):
    turtle.color(colors[a])
    x = 1

    for b in range(1, 100):
        turtle.forward(10)
        turtle.right(100 - x)
        x += 1