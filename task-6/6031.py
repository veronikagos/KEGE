from turtle import *
screensize(10000,10000)
tracer(0)
m = 40
lt(90)
rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
for x in range(-15,15):
    for y in range(-15,15):
        teleport(x * m, y * m)
        dot(3,'red')
update()
done()