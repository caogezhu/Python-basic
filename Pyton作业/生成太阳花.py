# 太阳花
import turtle
t = turtle.Turtle()
t.speed(0)
for _ in range(36):
    t.color("red", "yellow")
    t.begin_fill()
    t.forward(200)
    t.left(170)
    t.forward(200)
    t.left(20)
    t.end_fill()
turtle.done()
