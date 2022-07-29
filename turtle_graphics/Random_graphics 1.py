import turtle
import random
tim = turtle.Turtle()

colours = ["cornflower blue", "navy", "chartreuse", "lime", "yellow",
           "maroon", "light coral", "rosy brown", "medium orchid", "slate blue", "alice blue", "red", "yellow", "orange"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(70)
        tim.right(angle)


for shape_sides in range(4, 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_sides)
