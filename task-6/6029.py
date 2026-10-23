from turtle import *
screensize(10000,10000)
tracer(0)
m = 50
lt(90)

rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)
for x in range(-6,1):
    for y in range(-16,1):
        teleport(x * m, y * m)
        dot(3,'red')
print(6 * 5)
update()
done()