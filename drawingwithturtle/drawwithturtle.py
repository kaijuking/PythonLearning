import turtle


# Instructor's solution (which makes way more sense)
def draw_polygon(length, sides):
    angle = 360 / sides
    for i in range(sides):
        turtle.fd(length)
        turtle.lt(angle)


# My original approach
def draw_object():
    print("test")
    draw_square(50, 90)
    draw_triangle(50, 120)
    draw_triangle(50, -120)


def draw_square(length, angle):
    for i in range(4):
        turtle.fd(length)
        turtle.lt(angle)


def draw_triangle(length, angle):
    for i in range(3):
        turtle.fd(length)
        turtle.lt(angle)


if __name__ == "__main__":
    draw_object()

    polygon_list = [
        {"length": 100, "sides": 3},
        {"length": 100, "sides": 4},
        {"length": 100, "sides": 6},
        {"length": 100, "sides": 8},
        {"length": 100, "sides": 10}
    ]
    for i in range(len(polygon_list)):
        length = polygon_list[i]["length"]
        sides = polygon_list[i]["sides"]
        draw_polygon(length, sides)
