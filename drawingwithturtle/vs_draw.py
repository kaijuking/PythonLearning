import turtle

objects_to_draw = [{"sides": 4, "length": 10, "angle": 90}]

sides = objects_to_draw[0]["sides"]
length = objects_to_draw[0]["length"]
angle = objects_to_draw[0]["angle"]

for i in range(sides):
    turtle.fd(length)
    turtle.lt(angle)

turtle.done()