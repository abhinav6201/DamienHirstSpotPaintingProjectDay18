# import colorgram
#
# colors = colorgram.extract("image.jpg", 35)
#
# rgb_list = []
#
# for colors in colors:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)
import random
import turtle

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]

# TODO 1 - draw dot of size 20 - make dot of random color from color_list
# TODO 2 - move forward 50 space
# TODO 3 - repeat TODO 1 - run this loop for 10 times
# TODO 4 - return turtle to original position
# TODO 5 - repeat TODO 3 10 times and on starting of every loop put TODO 4

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed('fastest')
timmy.hideturtle()
timmy.penup()

screen = turtle.Screen()
# screen.setup(1920, 1080, 0, 0)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for i in range(10):
    turtle_orig_pos = timmy.pos()
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

    timmy.goto(turtle_orig_pos)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)

screen.exitonclick()
