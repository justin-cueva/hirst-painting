import turtle
from turtle import Screen
import random
# import colorgram
#
# colors = colorgram.extract('hirst_img.jpg', 20)
#
# rgb_colors = []
# for color in colors:
#     rgb_formatted = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb_formatted)
#
# print(rgb_colors)

color_list = [(62, 100, 150), (240, 83, 25), (175, 52, 34), (140, 30, 46), (75, 49, 41), (108, 171, 202),
              (174, 44, 50), (175, 180, 34), (237, 197, 68), (245, 214, 1), (226, 127, 58), (87, 34, 77),
              (85, 61, 39), (179, 146, 169), (99, 130, 159), (171, 188, 178)]

screen = Screen()
tim = turtle.Turtle()

screen.colormode(255)
tim.speed('fastest')
tim.penup()
tim.right(135)
tim.forward(325)
tim.left(135)
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50 * 10)
    tim.left(180)


turtle.exitonclick()
