from turtle import *
screensize(10000,10000)
tracer(0)
m = 10
lt(90)
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)
for x in range(10,18):
    for y in range(14,29):
        teleport(x * m, y * m)
        dot(3,'red')
print(8 * 15)
update()
done()