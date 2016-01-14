import turtle

screen = turtle.Screen()

turtle.speed('slow')
turtle.color('#FF69B4')
turtle.pensize(10)

length = int(input('Enter the length: '))
angle = int(input('Enter the angle: '))

print('Now enjoy :)')

while True:
    turtle.forward(length)
    turtle.right(angle)

screen.exitonclick()