from turtle import *
screensize(10000,10000)
tracer(0)
m = 10
lt(90)
for i in range(10):
    fd(22 * m)
    rt(90)
    fd(16 * m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(1 * m)
lt(90)
down()
for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)
for x in range(1,17):
    for y in range(1,23):
        teleport(x * m, y * m)
        dot(3, 'red')
print(2 * (15 + 21))
update()
done()