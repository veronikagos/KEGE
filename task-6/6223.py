from turtle import *
screensize(10000,10000)
tracer(0)
m = 5
lt(90)
for i in range(9):
    fd(17 * m)
    lt(90)
    fd(8 * m)
    lt(90)
    fd(17 * m)
up()
lt(90)
fd(3 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(4):
    fd(97 * m)
    rt(90)
    fd(132 * m)
    rt(90)
for x in range(-5,1):
    for y in range(-17,-4):
        teleport(x * m, y * m)
        dot(3, 'red')
print(5 * 2 + 12 * 2)
update()
done()