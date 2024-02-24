import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')

t.speed(50000)
n = 7000
h = 20

for i in range(200): 
    c = colorsys.hsv_to_rgb(h / 360, 1, 0.8)  
    t.color(c)
    t.left(2)
    t.fd(22)
    for j in range(1):
        t.left(50)
        t.circle(170)

turtle.done()  
