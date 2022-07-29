# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
import random
import turtle as turtle_module


turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(242, 236, 224), (127, 161, 196), (221, 234, 229), (207, 225, 233), (60, 93, 132), (198, 165, 93), (212, 132, 150), (203, 82, 103), (74, 109, 88), (245, 216, 221), (166, 58, 79), (145, 159, 62), (135, 172, 134), (23, 44, 70), (211,
                                                                                                                                                                                                                                                 205, 131), (142, 27, 47), (91, 123, 180), (129, 103, 50), (103, 149, 98), (226, 169, 179), (27, 54, 44), (32, 59, 112), (213, 79, 72), (41, 78, 63), (168, 200, 210), (173, 205, 171), (169, 191, 220), (42, 73, 79), (223, 176, 171), (88, 15, 28)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 144
for count in range(1, number_of_dots + 1):
    tim.dot(25, random.choice(color_list))
    tim.forward(50)

    if count % 12 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
