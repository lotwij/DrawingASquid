import turtle

Square = turtle.Turtle()
Square.color("black", "lightskyblue")
Square.pensize(5)

Square.forward(90)
Square.left(90)
Square.forward(90)
Square.left(90)
Square.forward(90)
Square.left(90)
Square.forward(90)
Square.left(90)

for x in range (4):
    Square.forward(90)
    Square.left(90)

##Define Function
def square():
    Square.forward(90)
    Square.left(90)
    Square.forward(90)
    Square.left(90)
    Square.forward(90)
    Square.left(90)
    Square.forward(90)
    Square.left(90)

square()

##Define Function Square with changable variable

def square(n):
    Square.forward(n)
    Square.left(90)
    Square.forward(n)
    Square.left(90)
    Square.forward(n)
    Square.left(90)
    Square.forward(n)
    Square.left(90)
square(200)

def square(n, i):
    Square.forward(n)
    Square.left(i)
    Square.forward(n)
    Square.left(i)
    Square.forward(n)
    Square.left(i)
    Square.forward(n)
    Square.left(i)
square(50,45)