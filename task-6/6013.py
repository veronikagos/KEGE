from turtle import *
screensize(10000,10000)
tracer(0)
m = 40
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
for i in range(2):
    rt(90)
    fd(10 * m)
for x in range(-14,8):
    for y in range(-14,8):
        teleport(x * m, y * m)
        dot(3,'red')
print(7 * 29)
update()
done()