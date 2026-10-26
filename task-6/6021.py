from turtle import *
screensize(10000,10000)
tracer(0)
m = 10

lt(90)
for i in range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)
for x in range(0,7):
    for y in range(0,4):
        teleport(x * m, y * m)
        dot(3,'red')
print(8 * 13 + 84 * 78 - 7 * 4)
update()
done()