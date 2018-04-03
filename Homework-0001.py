import turtle as tu


def house():
    for i in range(4):
        tu.pencolor("#E0E0E0")
        tu.forward(100)
        tu.left(90)

        tu.pensize(12)

    tu.penup()
    tu.goto(0, 100)
    tu.pendown()

    tu.pensize(12)
    tu.pencolor("#FF9999")

    for i in range(3):
        tu.color("#FF9999")
        tu.fillcolor("#FF9999")
        tu.begin_fill()
        tu.forward(100)
        tu.left(120)
        tu.end_fill()


house()


def tree1():
    tu.penup()
    tu.goto(-150, 0)
    tu.pendown()
    tu.pensize(12)
    tu.pencolor("brown")

    tu.left(90)
    tu.forward(80)
    tu.left(90)
    tu.forward(10)
    tu.left(90)
    tu.forward(80)

    tu.penup()
    tu.goto(-185, 100)
    tu.pendown()
    tu.begin_fill()
    tu.fillcolor("green")
    tu.pensize(12)
    tu.pencolor("green")
    tu.circle(30)
    tu.end_fill()


tree1()


def tree2():
    tu.penup()
    tu.goto(-300, 0)
    tu.pendown()
    tu.pensize(12)
    tu.pencolor("brown")
    tu.begin_fill()
    tu.fillcolor("brown")

    tu.right(180)
    tu.forward(100)
    tu.right(90)
    tu.forward(20)
    tu.right(90)
    tu.forward(100)
    tu.end_fill()

    tu.penup()
    tu.goto(-340, 120)
    tu.pendown()
    tu.begin_fill()
    tu.fillcolor("green")
    tu.pensize(12)
    tu.pencolor("green")
    tu.circle(50)
    tu.end_fill()


tree2()


def grass():
    tu.penup()
    tu.goto(-350, 0)
    tu.pendown()
    tu.pensize(12)
    tu.pencolor("green")
    tu.left(90)
    tu.forward(500)


grass()


def window():
    tu.penup()
    tu.goto(60, 60)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")

    for i in range(4):
        tu.pencolor("#E0E0E0")
        tu.forward(20)
        tu.left(90)
        tu.pensize(5)

    tu.penup()
    tu.goto(70, 60)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")
    tu.left(90)
    tu.forward(20)

    tu.penup()
    tu.goto(60, 70)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")
    tu.right(90)
    tu.forward(20)


window()


def sun():
    tu.penup()
    tu.goto(220, 210)
    tu.pendown()
    tu.pensize(9)
    tu.pencolor("yellow")
    tu.begin_fill()
    tu.fillcolor("yellow")
    tu.circle(40)
    tu.end_fill()


sun()


def door():
    tu.penup()
    tu.goto(70, 8)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")
    tu.begin_fill()
    tu.fillcolor("#E0E0E0")

    tu.left(90)
    tu.forward(40)
    tu.left(90)
    tu.forward(30)
    tu.left(90)
    tu.forward(40)
    tu.end_fill()


door()