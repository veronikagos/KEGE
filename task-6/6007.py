from turtle import *
screensize(10000,10000)
tracer(0)
m = 10
lt(90)
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
bk(6 * m)
rt(90)
fd(9 * m)
lt(90)
down()
for i in range(2):
    fd(17 * m)
    rt(90)
    fd(5 * m)
    rt(90)
for x in range(9,15):
    for y in range(0,11):
        teleport(x * m, y * m)
        dot(3,'red')
print(6 * 11)
update()
done()