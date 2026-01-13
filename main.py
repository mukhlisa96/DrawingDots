# import colorgram
# rgb_colors = []
# colors = colorgram.extract('Spot1.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode (255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(219, 235, 244), (220, 236, 230), (188, 157, 125), (227, 227, 204), (133, 82, 68), (142, 158, 177), (77, 95, 116), (17, 32, 51), (215, 212, 143), (134, 168, 145), (95, 117, 94), (236, 225, 230), (110, 143, 99), (179, 109, 91), (172, 145, 151), (68, 46, 40), (113, 78, 82), (35, 45, 44), (43, 59, 94), (122, 126, 138), (100, 48, 39), (161, 110, 114), (174, 201, 186), (57, 40, 43), (119, 137, 100), (178, 192, 208), (208, 181, 184), (210, 182, 178), (65, 65, 58), (94, 48, 54)]

tim.setheading(225)
tim.forward(300)
tim.setheading (0)

number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading (0)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading (180)
        tim.forward(500)
        tim.setheading (0)