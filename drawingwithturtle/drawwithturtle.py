import turtle


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
