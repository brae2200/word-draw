import turtle
#import mylib
#import random

def convert_letter_to_direction(pen):
    code_map = {"A": pen.forward(100), "B": pen.goto(100, 100), "C": turtle.circle(50), "D": turtle.dot()}

#def draw_a(pen):
    pen.up
    pen.goto(100, 100)
    pen.down

#if the message contains one of these, 

def draw_star(pen):
    pen.up

def draw_flower(pen):
    pen.up

def draw_cat(pen):
    pen.up


def art_dir():
    screen = turtle.Screen()
    screen.bgcolor('white')
    pen = turtle.Turtle()
    pen.speed(1)
    pen.pencolor('blue')

    pen.goto(100, 100)
    pen.forward(100)
    pen.left(90)
#will need to have the convert_letter_to_direction info return down here to give info to turtle
    #message= convert_letter_to_direction

    pen.hideturtle()
    #turtle.mainloop()
   
   #turtle.reset
   
   
def main():
    #message = input("Message: ")
    turtle.mainloop()

    
if __name__ == "__main__":
    main()