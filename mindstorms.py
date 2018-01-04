import turtle

def open_window():
    window = turtle.Screen()
    window.bgcolor("purple")

    square = turtle.Turtle()
    
    for i in range(0, 36):
        draw_square(square)
        square.right(10)
        
    #draw_circle()
    #draw_triangle()
    
    window.exitonclick()
    
def draw_square(some_turtle):

    some_turtle.color("cyan")
    some_turtle.shape("square")
    some_turtle.speed(5)

    for x in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    circle = turtle.Turtle()
    circle.color("grey")
    circle.shape("circle")
    circle.circle(100)

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.color("yellow")
    triangle.shape("triangle")

    for x in range(0, 3):
        triangle.backward(100)
        triangle.left(120)

open_window()
