import math
import turtle
turtle.speed(10)
turtle.penup()
turtle.goto(-50, -150)
turtle.pendown()


turtle.color('black')
turtle.begin_fill()
turtle.circle(200, -180)
turtle.circle(100, 180)
turtle.circle(-100, 180)
turtle.end_fill()

turtle.circle(-200, -180)
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.color('white')
turtle.dot(40)

turtle.penup()
turtle.goto(-50, 150)

turtle.pendown()
turtle.color('black')
turtle.dot(40)
def draw_bagua(x, y, radius):
    # 八卦的位置角度
    angles = [22.5 * i for i in range(8)]
    for i, angle in enumerate(angles):
        turtle.penup()
        # 计算每个卦象的中心位置
        turtle.goto(x + math.cos(math.radians(angle)) * (radius + 30), y + math.sin(math.radians(angle)) * (radius + 30))
        turtle.pendown()
        # 绘制三条横线
        for _ in range(3):
            turtle.forward(40)
            turtle.backward(40)
            turtle.right(120)

draw_bagua(-50, -50, 200)

turtle.done()