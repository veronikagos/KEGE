from turtle import *
screensize(1000, 1000)
tracer(0)
lt(90)
m = 5
for i in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)
for x in range(24,43):
    for y in range(0, 13):
        teleport(x * m, y * m)
        dot(3, 'red')
print(39 * 48 + 29 * 18 - 12 * 18)

update()
done()