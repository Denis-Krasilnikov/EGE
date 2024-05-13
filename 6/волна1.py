import turtle as t

t.up()
k = 20
t.tracer(10)
t.left(90)
t.down()
for i in range(2):
    t.forward(13*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.up()
t.forward(5*k)
t.right(90)
t.forward(9*k)
t.left(90)
t.down()
for i in range(2):
    t.forward(11*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)
t.up()
t.home()
for x in range(-40,40):
    for y in range(-40,40):
        t.goto(x*k,y*k)
        t.dot(2)
t.exitonclick()
