import math


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

p = (a + b + c)/2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(area)