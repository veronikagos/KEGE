from turtle import *

screensize(1000, 1000)
tracer(0)
m = 5

lt(90)
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()
fd(3 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(2):
    fd(70 * m)
    rt(90)
    fd(90 * m)
    rt(90)
for x in range(7,21): # 14
    for y in range(3,11): # 8
        teleport(x * m, y * m)
        dot(3,'red')

print(14*8)
update()
done()