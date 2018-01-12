import turtle

def open_window():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    flower = turtle.Turtle()

    draw_stem(flower)
    
    for i in range(0, 9):
        draw_large_circle(flower)
        flower.right(40)

    for i in range(0,9):
        draw_small_circle(flower)
        flower.right(40)

    for i in range(0,9):
        draw_smallest_circle(flower)
        flower.right(40)

    window.exitonclick()

def draw_stem(some_turtle):
    some_turtle.color("green")
    some_turtle.shape("circle")
    some_turtle.pensize(40)
    some_turtle.right(90)
    some_turtle.forward(300)
    some_turtle.backward(300)

def draw_large_circle(some_turtle):
    some_turtle.color("yellow")
    some_turtle.shape("circle")
    some_turtle.pensize(100)
    some_turtle.circle(100)

def draw_small_circle(some_turtle):
    some_turtle.color("red")
    some_turtle.shape("circle")
    some_turtle.pensize(40)
    some_turtle.circle(40)

def draw_smallest_circle(some_turtle):
    some_turtle.color("brown")
    some_turtle.shape("circle")
    some_turtle.pensize(25)
    some_turtle.circle(125)

open_window()
