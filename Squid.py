my_squid = turtle.Turtle()
my_squid.speed("fastest")
my_squid.color("black", "lightskyblue")
my_squid.pensize(5)

my_squid.goto(0,-10)

for x in range(13):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(-5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0,-10)
my_squid.left(-250)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(-5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0, 0)
my_squid.left(-140)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(-5)
    my_squid.forward(18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0, 0)
my_squid.left(140)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(-5)
    my_squid.forward(18)
    my_squid.pendown()


my_squid.penup()
my_squid.goto(0, 0)
my_squid.left(-50)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0, 0)
my_squid.left(-50)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0, -10)
my_squid.left(-50)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.goto(0, -10)
my_squid.left(-50)
my_squid.pendown()

for x in range(15):
    my_squid.begin_fill()
    my_squid.circle(10)
    my_squid.end_fill()
    my_squid.penup()
    my_squid.left(5)
    my_squid.forward(-18)
    my_squid.pendown()

my_squid.penup()
my_squid.left(80)
my_squid.goto(-10, -30)
my_squid.pendown()
my_squid.color("black", "lightskyblue")
my_squid.pensize(5)
my_squid.begin_fill()
my_squid.circle(100)
my_squid.end_fill()

my_squid.penup()
my_squid.goto(-45, 60)
my_squid.pendown()
my_squid.color("black", "white")
my_squid.pensize(3)
my_squid.begin_fill ()
my_squid.circle(28)
my_squid.end_fill()

my_squid.penup()
my_squid.goto(-45, 60)
my_squid.pendown()
my_squid.color("black", "black")
my_squid.pensize(3)
my_squid.begin_fill ()
my_squid.circle(20)
my_squid.end_fill()

my_squid.penup()
my_squid.goto(35, 60)
my_squid.pendown()
my_squid.color("black", "white")
my_squid.pensize(3)
my_squid.begin_fill ()
my_squid.circle(28)
my_squid.end_fill()

my_squid.penup()
my_squid.goto(35, 60)
my_squid.pendown()
my_squid.color("black", "black")
my_squid.pensize(3)
my_squid.begin_fill ()
my_squid.circle(20)
my_squid.end_fill()



turtle.Screen().mainloop()