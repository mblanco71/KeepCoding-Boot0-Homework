import turtle as tu


def house():
    for i in range(4):
        # Parte cuadrada de la casa

        # Pongo la tortuga
        tu.shape("turtle")
        # Primero decido color del lápiz
        tu.pencolor("#E0E0E0")
        tu.forward(100)
        tu.left(90)
        tu.pensize(12)

    # Moviendo el cursor hacia un nuevo punto
    tu.penup()
    tu.goto(0, 100)
    tu.pendown()

    # Cambiando el color y el tamaño del lápiz
    tu.pensize(12)
    tu.pencolor("#FF9999")

    for i in range(3):
        # Techo de la casa
        tu.color("#FF9999")
        # Rellenar el triángulo que forma el techo de la casa
        tu.fillcolor("#FF9999")
        tu.begin_fill()
        tu.forward(100)
        tu.left(120)
        tu.end_fill()


house()


def tree1():
    # tronco del arbol
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

    # Copa del arbol
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
    # tronco del arbol
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

    # Copa del arbol
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
    # Base de cesped
    tu.penup()
    tu.goto(-350, 0)
    tu.pendown()
    tu.pensize(12)
    tu.pencolor("green")
    tu.left(90)
    tu.forward(500)


grass()


def window():
    # Cuadrado de la ventana

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

    # Primera division de la ventana
    tu.penup()
    tu.goto(70, 60)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")
    tu.left(90)
    tu.forward(20)

    # Segunda division de la ventana
    tu.penup()
    tu.goto(60, 70)
    tu.pendown()
    tu.pensize(5)
    tu.pencolor("#E0E0E0")
    tu.right(90)
    tu.forward(20)


window()


def sun():
    # Haciendo el sol
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
    # Puerta de la casita
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


def bird1():
    # Primer amago de pájaro
    tu.penup()
    tu.goto(-200, 300)
    tu.pendown()

    tu.pensize(7)
    tu.pencolor("#295ea4")

    tu.color("#295ea4")
    tu.fillcolor("#295ea4")
    tu.forward(20)
    tu.left(120)
    tu.forward(20)


bird1()


def bird2():
    # Segundo pájaro
    tu.penup()
    tu.goto(-250, 350)
    tu.pendown()

    tu.pensize(7)
    tu.pencolor("#295ea4")

    tu.color("#295ea4")
    tu.fillcolor("#295ea4")
    tu.right(120)
    tu.forward(20)
    tu.right(120)
    tu.forward(20)


bird2()


def bird3():
    # Tercer pájaro
    tu.penup()
    tu.goto(-300, 300)
    tu.pendown()

    tu.pensize(7)
    tu.pencolor("#295ea4")

    tu.color("#295ea4")
    tu.fillcolor("#295ea4")
    tu.right(180)
    tu.forward(20)
    tu.left(120)
    tu.forward(20)


bird3()