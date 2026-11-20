from turtle import *
screensize(10000,10000)
tracer(0)
m = 30
lt(90)
for i in range(7):
    down()
    fd(10 * m)
    for n in range(4):
        rt(180)
        circle(2 * m,-180)
    bk(10 * m)
    for n in range(4):
        circle(2 * m,-180)
        rt(180)
for x in range(0,17):
    for y in range(-2,13):
        teleport(x * m, y * m)
        dot(3,'red')
print(6 * 8 + 9 * 15)
update()
done()