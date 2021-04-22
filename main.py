from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(242, 229, 78), (191, 9, 61), (209, 156, 93), (21, 115, 171), (172, 166, 24), (106, 178, 208), (167, 79, 30), (5, 29, 74), (216, 132, 166), (238, 223, 3), (224, 63, 113), (30, 135, 74), (122, 182, 141), (238, 72, 38), (177, 45, 94), (75, 11, 62), (7, 50, 25), (161, 21, 12), (66, 167, 96), (19, 166, 209), (77, 16, 4), (239, 160, 189), (15, 46, 133), (7, 102, 54), (136, 213, 228), (5, 89, 102)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(15,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()